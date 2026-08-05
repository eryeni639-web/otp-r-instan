import os
from dotenv import load_dotenv

load_dotenv()

OTP_API_KEY = os.getenv("OTPINSTAN_API_KEY")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")
