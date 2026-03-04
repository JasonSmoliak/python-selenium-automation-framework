import os
from dotenv import load_dotenv

# Load .env if present (does NOT override existing environment variables by default)
load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://example.com")
