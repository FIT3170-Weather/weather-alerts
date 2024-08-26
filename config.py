from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# API URLs
WEATHER_API_URL = "https://api.data.gov.my/weather/warning"
SUBSCRIPTIONS_API_URL = "http://127.0.0.1:8000/profiles/subscriptions"

# Email configuration
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))

# Other configuration
CACHE_FILE = "cache.json"
CHECK_INTERVAL = 300  # in seconds, i.e., 5 minutes
