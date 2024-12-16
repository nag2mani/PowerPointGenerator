# Slide Generator API

## Overview
**Slide Generator API** is an API-based project designed to automate the generation of professional slide presentations. It provides endpoints to create, retrieve, configure, and download presentations in PPTX format. The application is structured to ensure modularity and scalability, with a focus on efficient content generation and storage management.

## Video Link & Live App Link;

**Video Link**: https://drive.google.com/file/d/1aAFGqgPZJylkaSBQtEa13K-vso0uXP47/view?usp=sharing

**Deployed App Link**: https://pptgenerator.onrender.com

---

## Features
- **Create Presentations**: Generate presentations dynamically via API.
- **Retrieve Details**: Fetch metadata and configuration details of presentations.
- **Download PPTX**: Export and download presentations as PowerPoint files.
- **Configure Slides**: Update presentation configurations for customization.

---
## User Interface for Generating Slides
![image](https://github.com/user-attachments/assets/27b9156a-697f-44a2-b501-803cce0da7b3)

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
  "topic": "<string>",
  "num_slides": <integer>,
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
    ...
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
    ...
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
      ...
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

---

## Setup Instructions

### Prerequisites
- Python 3.8+
- Virtual Environment (recommended)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/a79.ai.git
   cd a79.ai/slide_generator_api
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the environment variables in `.env`:
   ```
   SECRET_KEY=your_secret_key
   DEBUG=True
   DATABASE_URL=your_database_url
   ```

5. Run the application:
   ```bash
   python app/main.py
   ```

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Contact
For queries or support, reach out to:
- Email: nag2mani@gmail.com
- GitHub: [nag2mani](https://github.com/nag2mani)

---
