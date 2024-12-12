# a79.ai

## Overview
**a79.ai** is an API-based project designed to automate the generation of professional slide presentations. It provides endpoints to create, retrieve, configure, and download presentations in PPTX format. The application is structured to ensure modularity and scalability, with a focus on efficient content generation and storage management.

---

## Features
- **Create Presentations**: Generate presentations dynamically via API.
- **Retrieve Details**: Fetch metadata and configuration details of presentations.
- **Download PPTX**: Export and download presentations as PowerPoint files.
- **Configure Slides**: Update presentation configurations for customization.

---

## API Endpoints

### 1. Create a New Presentation
**Endpoint:** `POST /api/v1/presentations`

**Description:**
Creates a new presentation with default or provided parameters.

**Request:**
```json
{
  "title": "My Presentation",
  "slides": [
    { "title": "Slide 1", "content": "Introduction" },
    { "title": "Slide 2", "content": "Details" }
  ]
}
```

**Response:**
```json
{
  "id": "12345",
  "status": "success",
  "message": "Presentation created successfully."
}
```

---

### 2. Retrieve Presentation Details
**Endpoint:** `GET /api/v1/presentations/{id}`

**Description:**
Fetches details of a presentation by ID.

**Response:**
```json
{
  "id": "12345",
  "title": "My Presentation",
  "slides": [...],
  "created_at": "YYYY-MM-DD HH:MM:SS"
}
```

---

### 3. Download Presentation
**Endpoint:** `GET /api/v1/presentations/{id}/download`

**Description:**
Downloads the presentation as a PPTX file.

**Response:**
Returns a downloadable PPTX file.

---

### 4. Modify Presentation Configuration
**Endpoint:** `POST /api/v1/presentations/{id}/configure`

**Description:**
Updates the configuration of a specific presentation.

**Request:**
```json
{
  "title": "Updated Presentation Title",
  "theme": "dark"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Configuration updated successfully."
}
```

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
- Email: nag2mani@example.com
- GitHub: [nag2mani](https://github.com/nag2mani)

---