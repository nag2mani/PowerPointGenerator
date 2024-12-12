import google.generativeai as genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

async def generate_content(topic: str, num_slides: int, custom_content: str = None):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Generate content for a {num_slides}-slide presentation on the topic: {topic}. "
    if custom_content:
        prompt += f"Include this custom content: {custom_content}. "
    prompt += "Format the output as a JSON array with each element representing a slide with 'title' and 'content' keys."

    try:
        response = await model.generate_content_async(prompt)
        content = response.text
        # Ensure the content is valid JSON
        json.loads(content)
        return content
    except Exception as e:
        raise Exception(f"Error generating content: {str(e)}")