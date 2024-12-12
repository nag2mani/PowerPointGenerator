from pptx import Presentation
from pptx.util import Inches, Pt
import json
import os

def generate_slides(content, presentation_id):
    prs = Presentation()
    content_json = json.loads(content)

    for i, slide_content in enumerate(content_json):
        slide_layout = prs.slide_layouts[1]  # Using a bullet layout for simplicity
        slide = prs.slides.add_slide(slide_layout)

        title = slide.shapes.title
        title.text = slide_content['title']

        content = slide.placeholders[1]
        content.text = slide_content['content']

    # Ensure the presentations directory exists
    os.makedirs('presentations', exist_ok=True)
    prs.save(f'presentations/{presentation_id}.pptx')
    return content_json