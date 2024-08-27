from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# API URLs
WEATHER_API_URL = "https://api.data.gov.my/weather/warning"
SUBSCRIPTIONS_API_URL = "http://127.0.0.1:8000/profiles/subscriptions"

# Email configuration
SEND_GRID_API_CLIENT = os.getenv('SEND_GRID_API_CLIENT')
FROM_EMAIL = os.getenv('FROM_EMAIL')

# Other configuration
CACHE_FILE = "cache.json"
CHECK_INTERVAL = 300  # in seconds, i.e., 5 minutes
