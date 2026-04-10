import os
from dotenv import load_dotenv
import requests

load_dotenv()
url = os.getenv("SLACK_WEBHOOK_URL")

print(f"Testing URL: {url}")
response = requests.post(url, json={"text": "Python Test Message!"})
print(f"Status: {response.status_code}, Response: {response.text}")
