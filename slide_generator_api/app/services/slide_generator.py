from pptx import Presentation
from pptx.util import Inches, Pt
import json
import os
import logging

def generate_slides(content, presentation_id="presentation"):
    prs = Presentation()

    # Parse content if it is a JSON string
    if isinstance(content, str):
        try:
            content_json = json.loads(content)
        except json.JSONDecodeError as e:
            logging.error(f"Invalid JSON format: {e}")
            return None
    else:
        content_json = content

    for i, slide_content in enumerate(content_json):
        slide = prs.slides.add_slide(prs.slide_layouts[1])  # Using bullet layout
        title_text = slide_content.get("title", f"Slide {i+1}")
        content_text = slide_content.get("content", [])

        # Title
        try:
            title = slide.shapes.title
            title.text = title_text
        except AttributeError:
            logging.warning(f"Slide {i+1} missing title placeholder.")

        # Content
        try:
            content = slide.placeholders[1]
            content.text_frame.clear()  # Clear default placeholder text
            if isinstance(content_text, str):
                content.text_frame.text = content_text
            elif isinstance(content_text, list):
                for point in content_text:
                    p = content.text_frame.add_paragraph()
                    p.text = point
                    p.font.size = Pt(18)  # Adjust font size if needed
            else:
                logging.warning(f"Unexpected content format on slide {i+1}.")
        except IndexError:
            logging.warning(f"Content placeholder missing on slide {i+1}.")

    presentations_dir = os.path.join(os.getcwd(), "presentations")
    os.makedirs(presentations_dir, exist_ok=True)
    output_path = os.path.join(presentations_dir, f"{presentation_id}.pptx")
    prs.save(output_path)
    logging.info(f"Presentation saved at '{output_path}'")
    return output_path

