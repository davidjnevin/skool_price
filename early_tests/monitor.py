import os
import time
import logging
from dotenv import load_dotenv
from scraper import get_skool_price # Import our new function

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def main():
    load_dotenv()
    url = os.getenv("SKOOL_URL")
    target_price = int(os.getenv("CORRECT_PRICE", "4800"))

    logging.info(f"Starting monitor for {url}. Target: ${target_price}")

    # For this test, we just run it ONCE
    current_price = get_skool_price(url)

    if current_price is not None:
        if current_price == target_price:
            logging.info(f"Check passed: Price is ${current_price}")
        else:
            logging.error(f"ALERT! Price is ${current_price}, expected ${target_price}")
    else:
        logging.error("Failed to retrieve price.")

if __name__ == "__main__":
    main()
