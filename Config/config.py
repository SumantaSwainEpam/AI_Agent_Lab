import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get Gemini API key from environment
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini client
genai.configure(api_key=API_KEY)

# Initialize Gemini model (Flash 2.0)
model = genai.GenerativeModel("gemini-1.5-flash")
