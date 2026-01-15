# PowerPoint Generator API

A production-ready, high-performance RESTful API that leverages cutting-edge AI technology to generate stunning, professional PowerPoint presentations automatically. Built with FastAPI and powered by Google's Gemini AI, this API delivers beautiful, colorful presentations with intelligent content generation and advanced formatting capabilities.

## API Response Times

- **Health Check**: < 10ms
- **Create Presentation**: 5-15 seconds (depends on AI generation)
- **Get Presentation**: < 50ms
- **Download Presentation**: < 100ms

---

## Sample Slides – Personal Finance

<table>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/8bdfa224-7098-4e67-885d-02bf8709767c" width="100%" />
    </td>
    <td>
      <img src="https://github.com/user-attachments/assets/b7e693a3-4373-41d7-819a-71e01efa57a7" width="100%" />
    </td>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/11bd218f-7faa-432f-bf8a-fd40bfc956b4" width="100%" />
    </td>
    <td>
      <img src="https://github.com/user-attachments/assets/c3d26d92-5c54-4468-a10d-f1f881ccf7a9" width="100%" />
    </td>
  </tr>
</table>

---

## Key Features

### Core Capabilities
- ✅ **AI-Powered Content Generation**: Automatically generates relevant, high-quality content for any topic
- ✅ **Beautiful Slide Design**: Professional, colorful presentations with gradient backgrounds
- ✅ **Markdown Support**: Automatically converts `**bold**` and `*italic*` to formatted text
- ✅ **Smart Content Management**: Handles long text, truncation, and proper spacing
- ✅ **Presentation CRUD**: Create, read, update, and download presentations
- ✅ **Health Monitoring**: Built-in health check endpoint for monitoring

### Advanced Features
- 🎨 **Dynamic Color Schemes**: Each slide gets a unique, vibrant color palette
- 📐 **Boundary Management**: All content stays within slide boundaries with proper margins
- 🔤 **Intelligent Text Formatting**: Supports markdown-style formatting in content
- 📊 **Flexible Configuration**: Customize number of slides, topics, and content
- 🎯 **Error Recovery**: Graceful error handling with detailed messages

---

## API Documentation

### Base URL
```
http://localhost:8000
```

### Interactive Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## API Endpoints

### 1. Health Check
**`GET /health`**

Check API health status.

**Response:**
```json
{
  "status": "healthy",
  "service": "PowerPoint Generator API"
}
```

---

### 2. API Information
**`GET /`**

Get API information and available endpoints.

**Response:**
```json
{
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
```

---

### 3. Create Presentation
**`POST /api/v1/presentations`**

Generate a new AI-powered presentation.

**Request Body:**
```json
{
  "topic": "Introduction to Python Programming",
  "num_slides": 5,
  "custom_content": "Focus on data science applications"
}
```

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `topic` | string | Yes | Main subject of the presentation |
| `num_slides` | integer | Yes | Number of slides to generate (default: 5) |
| `custom_content` | string | No | Additional context or requirements |

**Response (201 Created):**
```json
{
  "id": "040c4022-23da-4cee-a5b3-fa59cf2f0993",
  "message": "Presentation created successfully",
  "topic": "Introduction to Python Programming",
  "num_slides": 5,
  "download_url": "/api/v1/presentations/040c4022-23da-4cee-a5b3-fa59cf2f0993/download"
}
```

---

### 4. Get Presentation Details
**`GET /api/v1/presentations/{presentation_id}`**

Retrieve presentation metadata and content.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `presentation_id` | string | Unique presentation identifier |

**Response (200 OK):**
```json
{
  "id": "040c4022-23da-4cee-a5b3-fa59cf2f0993",
  "slides": [
    {
      "title": "Introduction to Python",
      "content": [
        "Python is a versatile programming language",
        "Widely used in data science and web development"
      ]
    }
  ]
}
```

---

### 5. Download Presentation
**`GET /api/v1/presentations/{presentation_id}/download`**

Download the generated PowerPoint file (.pptx).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `presentation_id` | string | Unique presentation identifier |

**Response:**
- Content-Type: `application/vnd.openxmlformats-officedocument.presentationml.presentation`
- File download: `presentation_{id}.pptx`

---

### 6. Configure Presentation
**`POST /api/v1/presentations/{presentation_id}/configure`**

Update an existing presentation with custom content.

**Request Body:**
```json
{
  "title": "Updated Presentation Title",
  "slides": [
    {
      "title": "Slide 1",
      "content": ["Point 1", "Point 2", "Point 3"]
    },
    {
      "title": "Slide 2",
      "content": ["Point A", "Point B"]
    }
  ]
}
```

**Response (200 OK):**
```json
{
  "message": "Presentation updated successfully",
  "presentation": {
    "id": "...",
    "title": "Updated Presentation Title",
    "slides": [...]
  }
}
```

---

## Quick Start

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/nag2mani/PowerPointGenerator.git
   cd PowerPointGenerator
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   Create a `.env` file:
   ```env
   GOOGLE_API_KEY=your_google_gemini_api_key_here
   ```

5. **Run the API server**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

6. **Access the API**
   - API: http://localhost:8000
   - Interactive Docs: http://localhost:8000/docs
   - Health Check: http://localhost:8000/health

---

## 📁 Project Structure

```
PowerPointGenerator/
├── app/
│   ├── __init__.py                 # Application package
│   ├── main.py                     # FastAPI application & routes
│   ├── models.py                   # Data models
│   ├── services/                   # Business logic layer
│   │   ├── __init__.py
│   │   ├── content_generator.py    # AI content generation service
│   │   └── slide_generator.py      # PowerPoint generation service
│   └── utils/                      # Utility functions
│       ├── __init__.py
│       └── storage.py              # Presentation storage management
├── presentations/                  # Generated presentation files
├── requirements.txt                # Python dependencies
├── .env                           # Environment configuration
└── README.md                       # This file
```

---

## 🛠️ Technology Stack

- **Framework**: FastAPI - Modern, fast web framework for building APIs
- **AI Engine**: Google Gemini 2.5 Flash - Latest AI model for content generation
- **Presentation Library**: python-pptx - Professional PowerPoint generation
- **Validation**: Pydantic - Data validation using Python type annotations
- **Server**: Uvicorn - Lightning-fast ASGI server
- **Environment**: python-dotenv - Environment variable management

---

## Design Features

### Color Palettes
Each slide automatically gets a unique, vibrant gradient:
- 🔵 Blue to Purple
- 🟠 Orange to Pink
- 🔷 Teal to Blue
- 🟢 Green to Teal
- 🟣 Purple to Blue
- 🔴 Red to Orange
- 🟦 Indigo to Purple
- 🔷 Cyan to Blue

### Typography
- **Title Font**: 38pt, Bold, White
- **Content Font**: 20-22pt, White
- **Bullet Points**: Styled with proper spacing
- **Markdown Support**: `**bold**` and `*italic*` automatically formatted

### Layout
- **Safe Margins**: 0.75" on all sides
- **Content Containment**: Automatic text truncation and wrapping
- **Professional Spacing**: Optimized line heights and paragraph spacing
- **Visual Accents**: Decorative elements for enhanced aesthetics

---

## Example Usage

### Using cURL

```bash
# Create a presentation
curl -X POST http://localhost:8000/api/v1/presentations \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Introduction to Machine Learning",
    "num_slides": 5,
    "custom_content": "Focus on neural networks"
  }'

# Get presentation details
curl http://localhost:8000/api/v1/presentations/{presentation_id}

# Download presentation
curl http://localhost:8000/api/v1/presentations/{presentation_id}/download \
  --output presentation.pptx
```

### Using Python

```python
import requests

# Create presentation
response = requests.post(
    "http://localhost:8000/api/v1/presentations",
    json={
        "topic": "Python Best Practices",
        "num_slides": 3
    }
)
presentation_id = response.json()["id"]

# Download presentation
download_url = f"http://localhost:8000/api/v1/presentations/{presentation_id}/download"
file_response = requests.get(download_url)
with open("presentation.pptx", "wb") as f:
    f.write(file_response.content)
```

### Using JavaScript/Fetch

```javascript
// Create presentation
const response = await fetch('http://localhost:8000/api/v1/presentations', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    topic: 'Web Development Trends',
    num_slides: 4
  })
});

const data = await response.json();
const presentationId = data.id;

// Download presentation
window.location.href = `http://localhost:8000/api/v1/presentations/${presentationId}/download`;
```


**Built with ❤️ using FastAPI and Google Gemini AI**
