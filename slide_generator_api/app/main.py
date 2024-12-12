import uuid
import uvicorn
from pydantic import BaseModel
from typing import List, Optional
from fastapi.responses import FileResponse
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.services.slide_generator import generate_slides
from app.services.content_generator import generate_content
from app.utils.storage import save_presentation, get_presentation, update_presentation
import logging
import os

app = FastAPI()

logging.basicConfig(level=logging.ERROR) #For better Error Logging

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the static directory
app.mount("/static", StaticFiles(directory="app/static"), name="static")

class PresentationCreate(BaseModel):
    topic: str
    num_slides: int = 5
    custom_content: Optional[str] = None

class PresentationConfigure(BaseModel):
    title: str
    slides: list[str]

# Add a root route to serve the index.html file
@app.get("/")
async def read_root():
    file_path = os.path.join(os.path.dirname(__file__), "static", "index.html")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="index.html not found")
    return FileResponse(file_path)


@app.post("/api/v1/presentations")
async def create_presentation(presentation: PresentationCreate):
    try:
        presentation_id = str(uuid.uuid4())
        
        # Await the asynchronous generate_content function
        content = await generate_content(presentation.topic, presentation.num_slides, presentation.custom_content)
        # print(content)
        slides = generate_slides(content, presentation_id)  # Assuming generate_slides is synchronous
        save_presentation(presentation_id, slides)
        
        return {"id": presentation_id, "message": "Presentation created successfully"}
    except Exception as e:
        logging.error(f"Error creating presentation: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while creating the presentation.")


@app.get("/api/v1/presentations/{presentation_id}")
async def get_presentation_details(presentation_id: str):
    presentation = get_presentation(presentation_id)
    if not presentation:
        raise HTTPException(status_code=404, detail="Presentation not found")
    return presentation


@app.get("/api/v1/presentations/{presentation_id}/download")
async def download_presentation(presentation_id: str):
    presentation = get_presentation(presentation_id)
    if not presentation:
        raise HTTPException(status_code=404, detail="Presentation not found")
    # file_path = f"presentations/{presentation_id}.pptx"
    file_path = os.path.join(os.getcwd(), "presentations", f"{presentation_id}.pptx")
    return FileResponse(file_path, filename=f"presentation_{presentation_id}.pptx")


@app.post("/api/v1/presentations/{presentation_id}/configure")
async def configure_presentation(presentation_id: str, config: PresentationConfigure):
    presentation = get_presentation(presentation_id)
    if not presentation:
        raise HTTPException(status_code=404, detail="Presentation not found")
    # Update the presentation using the provided configuration
    updated_presentation = update_presentation(presentation_id, {"slides": config.slides})
    if not updated_presentation:
        raise HTTPException(status_code=400, detail="Unable to update the presentation")
    return {"message": "Presentation updated successfully", "presentation": updated_presentation}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)