import logging
import requests
from bs4 import BeautifulSoup

def get_skool_price(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # We search for the span inside the div with the specific class
        # Note: We use a partial match for the class to be safer
        info_item = soup.find('div', class_='styled__InfoItem')

        if info_item:
            price_text = info_item.find('span').text
            # price_text is currently "$4,800/year"
            # We need to turn this into a clean number: 4800
            clean_price = "".join(filter(str.isdigit, price_text))
            return int(clean_price)

        logging.warning("Could not find the price element on the page.")
        return None

    except Exception as e:
        logging.error(f"Scraping error: {e}")
        return None
