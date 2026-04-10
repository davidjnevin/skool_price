import os
import time
import logging
from dotenv import load_dotenv
from scraper import get_skool_price

# Professional logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def main():
    load_dotenv()

    # Configuration from ENV
    url = os.getenv("SKOOL_URL")
    target_price = int(os.getenv("CORRECT_PRICE", "4800"))
    threshold = int(os.getenv("ALERT_THRESHOLD", "5")) # Default to 5 if not found

    # State management
    wrong_price_count = 0
    alert_sent = False

    logging.info(f"Monitor active for: {url}")
    logging.info(f"Target: ${target_price} | Threshold: {threshold} mins")

    while True:
        current_price = get_skool_price(url)

        if current_price is not None:
            if current_price != target_price:
                wrong_price_count += 1
                logging.warning(
                    f"Price mismatch! Observed: ${current_price}. "
                    f"Strike {wrong_price_count}/{threshold}"
                )
            else:
                if wrong_price_count > 0:
                    logging.info("Price returned to normal. Resetting counter.")
                wrong_price_count = 0
                alert_sent = False

        # Logic: Compare counter against our new ENV threshold
        if wrong_price_count >= threshold and not alert_sent:
            logging.critical(f"PRICE WRONG FOR {threshold} MINUTES. TRIGGERING ALERT...")
            # send_slack_alert(current_price) <--- Next Step
            alert_sent = True

        time.sleep(60)

if __name__ == "__main__":
    main()
