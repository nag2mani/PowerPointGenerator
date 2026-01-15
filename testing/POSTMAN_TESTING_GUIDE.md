# Postman Testing Guide for PowerPoint Generator API

## Quick Start

1. **Import the Collection**: 
   - Open Postman
   - Click "Import" button
   - Select `POSTMAN_COLLECTION.json` file
   - The collection will be imported with all endpoints pre-configured

2. **Start the API Server**:
   ```bash
   cd /Users/nagmani/nag2mani/development/PowerPointGenerator
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

3. **Base URL**: `http://localhost:8000`

---

## API Endpoints

### 1. Health Check
- **Method**: `GET`
- **URL**: `http://localhost:8000/health`
- **Description**: Check if the API is running
- **Response**: 
  ```json
  {
    "status": "healthy",
    "service": "PowerPoint Generator API"
  }
  ```

### 2. Root - API Information
- **Method**: `GET`
- **URL**: `http://localhost:8000/`
- **Description**: Get API information and available endpoints
- **Response**: JSON with API details and endpoint list

### 3. Create Presentation ⭐
- **Method**: `POST`
- **URL**: `http://localhost:8000/api/v1/presentations`
- **Headers**: 
  ```
  Content-Type: application/json
  ```
- **Body** (JSON):
  ```json
  {
    "topic": "Introduction to Python Programming",
    "num_slides": 5,
    "custom_content": "Focus on data science and web development"
  }
  ```
- **Response** (201 Created):
  ```json
  {
    "id": "040c4022-23da-4cee-a5b3-fa59cf2f0993",
    "message": "Presentation created successfully",
    "topic": "Introduction to Python Programming",
    "num_slides": 5,
    "download_url": "/api/v1/presentations/040c4022-23da-4cee-a5b3-fa59cf2f0993/download"
  }
  ```
- **Note**: Save the `id` from the response for other endpoints!

### 4. Get Presentation Details
- **Method**: `GET`
- **URL**: `http://localhost:8000/api/v1/presentations/{presentation_id}`
- **Example**: `http://localhost:8000/api/v1/presentations/040c4022-23da-4cee-a5b3-fa59cf2f0993`
- **Response**:
  ```json
  {
    "id": "040c4022-23da-4cee-a5b3-fa59cf2f0993",
    "slides": [
      {
        "title": "Introduction to Python",
        "content": ["Point 1", "Point 2"]
      }
    ]
  }
  ```

### 5. Download Presentation
- **Method**: `GET`
- **URL**: `http://localhost:8000/api/v1/presentations/{presentation_id}/download`
- **Example**: `http://localhost:8000/api/v1/presentations/040c4022-23da-4cee-a5b3-fa59cf2f0993/download`
- **Response**: Downloads a `.pptx` file
- **Note**: In Postman, click "Send and Download" to save the file

### 6. Configure Presentation
- **Method**: `POST`
- **URL**: `http://localhost:8000/api/v1/presentations/{presentation_id}/configure`
- **Headers**: 
  ```
  Content-Type: application/json
  ```
- **Body** (JSON):
  ```json
  {
    "title": "Updated Presentation Title",
    "slides": [
      {
        "title": "Slide 1 Title",
        "content": ["Point 1", "Point 2", "Point 3"]
      },
      {
        "title": "Slide 2 Title",
        "content": ["Point A", "Point B"]
      }
    ]
  }
  ```
- **Response**:
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

## Testing Workflow

### Complete Flow Example:

1. **Health Check** → Verify API is running
2. **Create Presentation** → Get a `presentation_id`
3. **Get Presentation Details** → View the generated content
4. **Download Presentation** → Get the PowerPoint file
5. **Configure Presentation** (Optional) → Update if needed

---

## Interactive API Documentation

FastAPI provides automatic interactive documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

You can test all endpoints directly from the browser using these interfaces!

---

## Common Issues

1. **404 Not Found**: Make sure the server is running
2. **500 Internal Server Error**: Check if `GOOGLE_API_KEY` is set in `.env` file
3. **Connection Refused**: Verify the server is running on port 8000

---

## Environment Variables

Make sure your `.env` file contains:
```
GOOGLE_API_KEY=your_api_key_here
```
