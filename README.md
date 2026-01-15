# PowerPoint Generator

## Overview
**PowerPoint Generator** is an API-based project designed to automate the generation of professional slide presentations. It provides endpoints to create, retrieve, configure, and download presentations in PPTX format. The application is structured to ensure modularity and scalability, with a focus on efficient content generation and storage management.

**Deployed App Link**: https://pptgenerator.onrender.com

## User Interface;

![image](https://github.com/user-attachments/assets/adbf062a-f0a6-416e-b0fb-d4161dd0452b)

---

## Features
- **Create Presentations**: Generate presentations dynamically via API.
- **Retrieve Details**: Fetch metadata and configuration details of presentations.
- **Download PPTX**: Export and download presentations as PowerPoint files.
- **Configure Slides**: Update presentation configurations for customization.

---

## Directory Structure
```
slide_generator_api/
├── app/
│   ├── __init__.py             # Application initialization
│   ├── main.py                 # Entry point of the API
│   ├── models.py               # Database models
│   ├── services/               # Core business logic
│   │   ├── __init__.py
│   │   ├── content_generator.py # Generates content for slides
│   │   └── slide_generator.py   # Generates slide layouts
│   ├── utils/                  # Utility modules
│   │   ├── __init__.py
│   │   └── storage.py           # Handles file storage
│   └── static/
│       └── index.html          # HTML template for front-end (if any)
├── requirements.txt            # Python dependencies
└── .env                        # Environment configuration
```

---

## API Endpoints


### 1. Create a Presentation

**URL:** `/presentations`

**Method:** `POST`

**Description:** Creates a new presentation with generated content and saves it.

#### Request Body (JSON):
```json
{
  "topic": "<String>",
  "num_slides": "<Integer>",
  "custom_content": "<string (optional)>"
}
```

| Parameter       | Type    | Required | Description                                     |
|-----------------|---------|----------|-------------------------------------------------|
| `topic`         | string  | Yes      | The topic of the presentation.                 |
| `num_slides`    | integer | Yes      | Number of slides to generate.                  |
| `custom_content`| string  | No       | Optional custom content to include in slides.  |

#### Response (200 OK):
```json
{
  "id": "<string>",
  "message": "Presentation created successfully"
}
```

#### Error Response (500 Internal Server Error):
```json
{
  "detail": "An error occurred while creating the presentation."
}
```

---

### 2. Get Presentation Details

**URL:** `/presentations/{presentation_id}`

**Method:** `GET`

**Description:** Retrieves the details of a specific presentation.

#### Path Parameter:
| Parameter         | Type    | Description                         |
|-------------------|---------|-------------------------------------|
| `presentation_id` | string  | The ID of the presentation to fetch.|

#### Response (200 OK):
```json
{
  "id": "<string>",
  "slides": [
    {
      "title": "<string>",
      "content": "<string>"
    },
  ]
}
```

#### Error Response (404 Not Found):
```json
{
  "detail": "Presentation not found"
}
```

---

### 3. Download Presentation

**URL:** `/presentations/{presentation_id}/download`

**Method:** `GET`

**Description:** Downloads the generated presentation as a `.pptx` file.

#### Path Parameter:
| Parameter         | Type    | Description                         |
|-------------------|---------|-------------------------------------|
| `presentation_id` | string  | The ID of the presentation to fetch.|

#### Response (File Download):
- A `.pptx` file with the generated presentation.

#### Error Response (404 Not Found):
```json
{
  "detail": "Presentation not found"
}
```

---

### 4. Configure Presentation

**URL:** `/presentations/{presentation_id}/configure`

**Method:** `POST`

**Description:** Updates an existing presentation's slides using provided configurations.

#### Path Parameter:
| Parameter         | Type    | Description                         |
|-------------------|---------|-------------------------------------|
| `presentation_id` | string  | The ID of the presentation to update.|

#### Request Body (JSON):
```json
{
  "slides": [
    {
      "title": "<string>",
      "content": "<string>"
    },
  ]
}
```

| Parameter   | Type  | Required | Description                        |
|-------------|-------|----------|------------------------------------|
| `slides`    | array | Yes      | An array of slide objects to update.|

#### Response (200 OK):
```json
{
  "message": "Presentation updated successfully",
  "presentation": {
    "id": "<string>",
    "slides": [
      {
        "title": "<string>",
        "content": "<string>"
      },
    ]
  }
}
```

#### Error Responses:
- **404 Not Found:**
  ```json
  {
    "detail": "Presentation not found"
  }
  ```
- **400 Bad Request:**
  ```json
  {
    "detail": "Unable to update the presentation"
  }
  ```

---

## Setup and Running the API

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set the `GOOGLE_API_KEY` in the `.env` file.
3. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
