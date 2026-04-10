import json
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

        # 1. Find the script tag containing the JSON data
        script_tag = soup.find('script', id='__NEXT_DATA__')

        if script_tag:
            # 2. Parse the text inside the script tag as JSON
            data = json.loads(script_tag.string)

            # 3. Navigate the dictionary to find the displayPrice
            # Based on your source code: props -> pageProps -> currentGroup -> metadata -> displayPrice
            group_metadata = data['props']['pageProps']['currentGroup']['metadata']
            display_price_raw = group_metadata.get('displayPrice')

            if display_price_raw:
                # The price is stored as a stringified JSON: '{"currency":"usd","amount":480000...}'
                price_data = json.loads(display_price_raw)

                # Skool stores $4,800 as 480000 (in cents)
                amount_in_cents = price_data.get('amount')
                return amount_in_cents // 100  # Convert to dollars

        logging.warning("Could not find the price data in the JSON payload.")
        return None

    except Exception as e:
        logging.error(f"Data extraction error: {e}")
        return None
