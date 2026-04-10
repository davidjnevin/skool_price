import requests
from dotenv import load_dotenv

load_dotenv()
URL = "YOUR_SKOOL_COMMUNITY_URL_HERE"

# We add a 'User-Agent' so we look like a Chrome browser, not a script
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36'
}

response = requests.get(URL, headers=headers)

print(f"Status Code: {response.status_code}") # 200 means success
print(response.text[:500]) # Print the first 500 characters of the page code
