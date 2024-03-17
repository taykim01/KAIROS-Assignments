from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)
chat = client.chat.completions