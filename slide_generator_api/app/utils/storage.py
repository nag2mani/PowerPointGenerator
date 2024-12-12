presentations = {}

def save_presentation(presentation_id: str, slides: list):
    presentations[presentation_id] = {
        "id": presentation_id,
        "slides": slides
    }

def get_presentation(presentation_id: str):
    return presentations.get(presentation_id)

def update_presentation(presentation_id: str, updates: dict):
    if presentation_id in presentations:
        presentations[presentation_id].update(updates)
        return presentations[presentation_id]
    return None