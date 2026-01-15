import uuid
import uvicorn
from pydantic import BaseModel
from typing import List, Optional, Dict
from fastapi.responses import FileResponse, JSONResponse
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.services.slide_generator import generate_slides
from app.services.content_generator import generate_content
from app.utils.storage import save_presentation, get_presentation, update_presentation
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app with API metadata
app = FastAPI(
    title="PowerPoint Generator API",
    description="A RESTful API for generating PowerPoint presentations using AI",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware for API access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response Models
class PresentationCreate(BaseModel):
    topic: str
    num_slides: int = 5
    custom_content: Optional[str] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "topic": "Introduction to Python",
                "num_slides": 5,
                "custom_content": "Focus on data science applications"
            }
        }

class SlideContent(BaseModel):
    title: str
    content: List[str]

class PresentationConfigure(BaseModel):
    title: str
    slides: List[SlideContent]
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "My Presentation",
                "slides": [
                    {
                        "title": "Slide 1",
                        "content": ["Point 1", "Point 2"]
                    }
                ]
            }
        }

# Root endpoint - API information
@app.get("/", tags=["Root"])
async def root():
    """API root endpoint with basic information"""
    return {
        "message": "PowerPoint Generator API",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "create_presentation": "POST /api/v1/presentations",
            "get_presentation": "GET /api/v1/presentations/{id}",
            "download_presentation": "GET /api/v1/presentations/{id}/download",
            "configure_presentation": "POST /api/v1/presentations/{id}/configure"
        }
    }

# Health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "PowerPoint Generator API"}


@app.post("/api/v1/presentations", tags=["Presentations"], status_code=201)
async def create_presentation(presentation: PresentationCreate):
    """
    Create a new PowerPoint presentation
    
    - **topic**: The main topic/subject of the presentation
    - **num_slides**: Number of slides to generate (default: 5)
    - **custom_content**: Optional custom content to include in the presentation
    """
    try:
        presentation_id = str(uuid.uuid4())
        logger.info(f"Creating presentation: {presentation_id} for topic: {presentation.topic}")
        
        # Generate content using AI
        content = await generate_content(
            presentation.topic, 
            presentation.num_slides, 
            presentation.custom_content
        )
        
        # Generate PowerPoint file
        file_path = generate_slides(content, presentation_id)
        
        # Save presentation metadata
        save_presentation(presentation_id, content)
        
        return {
            "id": presentation_id,
            "message": "Presentation created successfully",
            "topic": presentation.topic,
            "num_slides": len(content),
            "download_url": f"/api/v1/presentations/{presentation_id}/download"
        }
    except Exception as e:
        logger.error(f"Error creating presentation: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500, 
            detail=f"An error occurred while creating the presentation: {str(e)}"
        )


@app.get("/api/v1/presentations/{presentation_id}", tags=["Presentations"])
async def get_presentation_details(presentation_id: str):
    """
    Get details of a specific presentation
    
    - **presentation_id**: The unique identifier of the presentation
    """
    presentation = get_presentation(presentation_id)
    if not presentation:
        raise HTTPException(status_code=404, detail="Presentation not found")
    return presentation


@app.get("/api/v1/presentations/{presentation_id}/download", tags=["Presentations"])
async def download_presentation(presentation_id: str):
    """
    Download a presentation as a PowerPoint (.pptx) file
    
    - **presentation_id**: The unique identifier of the presentation
    """
    presentation = get_presentation(presentation_id)
    if not presentation:
        raise HTTPException(status_code=404, detail="Presentation not found")
    
    file_path = os.path.join(os.getcwd(), "presentations", f"{presentation_id}.pptx")
    
    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404, 
            detail="Presentation file not found. The presentation may not have been generated successfully."
        )
    
    return FileResponse(
        file_path, 
        filename=f"presentation_{presentation_id}.pptx",
        media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation"
    )


@app.post("/api/v1/presentations/{presentation_id}/configure", tags=["Presentations"])
async def configure_presentation(presentation_id: str, config: PresentationConfigure):
    """
    Update/configure an existing presentation
    
    - **presentation_id**: The unique identifier of the presentation
    - **title**: New title for the presentation
    - **slides**: List of slides with title and content
    """
    presentation = get_presentation(presentation_id)
    if not presentation:
        raise HTTPException(status_code=404, detail="Presentation not found")
    
    # Convert slides to the format expected by storage
    slides_data = [{"title": slide.title, "content": slide.content} for slide in config.slides]
    
    # Update the presentation
    updated_presentation = update_presentation(
        presentation_id, 
        {"title": config.title, "slides": slides_data}
    )
    
    if not updated_presentation:
        raise HTTPException(status_code=400, detail="Unable to update the presentation")
    
    return {
        "message": "Presentation updated successfully", 
        "presentation": updated_presentation
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)