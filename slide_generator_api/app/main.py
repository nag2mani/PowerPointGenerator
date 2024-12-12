import uuid
from pydantic import BaseModel
from typing import List, Optional
from fastapi.responses import FileResponse
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.services.slide_generator import generate_slides
from app.services.content_generator import generate_content
from app.utils.storage import save_presentation, get_presentation, update_presentation

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Mount the static directory
app.mount("/static", StaticFiles(directory="app/static"), name="static")

class PresentationCreate(BaseModel):
    topic: str
    num_slides: int = 5
    custom_content: Optional[str] = None

class PresentationConfigure(BaseModel):
    num_slides: Optional[int] = None
    layout: Optional[str] = None
    theme: Optional[str] = None
    font: Optional[str] = None
    color: Optional[str] = None

# Add a root route to serve the index.html file
@app.get("/")
async def read_root():
    return FileResponse("app/static/index.html")

@app.post("/api/v1/presentations")
async def create_presentation(presentation: PresentationCreate):
    try:
        presentation_id = str(uuid.uuid4())
        content = await generate_content(presentation.topic, presentation.num_slides, presentation.custom_content)
        slides = generate_slides(content, presentation_id)
        save_presentation(presentation_id, slides)
        return {"id": presentation_id, "message": "Presentation created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

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
    file_path = f"presentations/{presentation_id}.pptx"
    return FileResponse(file_path, filename=f"presentation_{presentation_id}.pptx")

@app.post("/api/v1/presentations/{presentation_id}/configure")
async def configure_presentation(presentation_id: str, config: PresentationConfigure):
    presentation = get_presentation(presentation_id)
    if not presentation:
        raise HTTPException(status_code=404, detail="Presentation not found")
    updated_presentation = update_presentation(presentation_id, config.dict(exclude_unset=True))
    return {"message": "Presentation updated successfully", "presentation": updated_presentation}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)