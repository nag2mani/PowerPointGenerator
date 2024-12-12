import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
import logging
import asyncio

# Load environment variables
load_dotenv()

# Configure the Generative AI client
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

async def generate_content(topic: str, num_slides: int, custom_content: str = None):
    """
    Generates content for a slide presentation using Google's Generative AI.

    Args:
        topic (str): The topic for the presentation.
        num_slides (int): The number of slides to generate.
        custom_content (str, optional): Custom content to include in the presentation.

    Returns:
        list: A list of dictionaries, each representing a slide with a title and content.

    Raises:
        Exception: If there are issues with content generation or validation.
    """
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Create the prompt for the AI model
    prompt = (
        f"Generate content for a {num_slides}-slide presentation on the topic: '{topic}'. "
        "Each slide should include a 'title' and 'content'. "
    )
    if custom_content:
        prompt += f"Include this custom content: {custom_content}. "
    prompt += "Format the output as a valid JSON array where each element is a dictionary "
    prompt += "with 'title' as a string and 'content' as a list of strings."

    try:
        # Generate content asynchronously
        response = await model.generate_content_async(prompt)

        if not response.text:
            raise ValueError("Received empty response from the model.")

        raw_content = response.text.strip()
        logging.debug(f"Raw response content: {raw_content}")

        # Clean the response to extract valid JSON
        cleaned_content = raw_content.replace("```json", "").replace("```", "").strip()
        logging.debug(f"Cleaned response content: {cleaned_content}")

        # Validate and parse the JSON response
        try:
            json_content = json.loads(cleaned_content)

            # Ensure the JSON is a list of dictionaries with required keys
            if not isinstance(json_content, list):
                raise ValueError("Generated content is not a JSON array.")
            for item in json_content:
                if not isinstance(item, dict):
                    raise ValueError("Each item in the array must be a dictionary.")
                if 'title' not in item or 'content' not in item:
                    raise ValueError("Each dictionary must have 'title' and 'content' keys.")
                if not isinstance(item['content'], list) or not all(isinstance(line, str) for line in item['content']):
                    raise ValueError("'content' must be a list of strings.")

            return json_content

        except json.JSONDecodeError as e:
            logging.error(f"JSON decoding error: {e}")
            logging.error(f"Invalid response content: {cleaned_content}")
            raise Exception("Invalid JSON format from the model.")
        except ValueError as ve:
            logging.error(f"Validation error: {ve}")
            raise Exception("Invalid content structure.")

    except Exception as e:
        logging.error(f"Error generating content: {e}")
        raise Exception(f"Error generating content: {e}")

# Example usage (within an async context)
async def main():
    topic = "Introduction to Python"
    num_slides = 3
    custom_content = "Include examples of Python applications in data science."

    try:
        slides = await generate_content(topic, num_slides, custom_content)
        print(json.dumps(slides, indent=4))
    except Exception as e:
        print(f"Failed to generate slides: {e}")

# Entry point for the script
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)  # Enable debug logging
    asyncio.run(main())
