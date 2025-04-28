from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env file

api_key = os.getenv("OPENAI_API_KEY")
print(api_key)  # now you can use it safely
