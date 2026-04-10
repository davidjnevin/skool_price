import os
import logging
import requests
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def check_connectivity(url):
    """Verifies the script can reach the Skool page."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # Raises error for 4xx or 5xx codes
        logging.info(f"Connection Successful. Status Code: {response.status_code}")
        return True
    except requests.exceptions.RequestException as e:
        logging.error(f"Connection Failed: {e}")
        return False

def main():
    load_dotenv()
    url = os.getenv("SKOOL_URL")

    if not url:
        logging.critical("SKOOL_URL not found in .env file!")
        return

    check_connectivity(url)

if __name__ == "__main__":
    main()
