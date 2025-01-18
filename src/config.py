import os
from dotenv import load_dotenv

load_dotenv()  # Încarcă variabilele din .env

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SALESFORCE_USERNAME = os.getenv("SALESFORCE_USERNAME")
SALESFORCE_PASSWORD = os.getenv("SALESFORCE_PASSWORD")
SALESFORCE_TOKEN = os.getenv("SALESFORCE_TOKEN")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
