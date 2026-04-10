import os
import time
import logging
from dotenv import load_dotenv
from scraper import get_skool_price

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def main():
    load_dotenv()
    url = os.getenv("SKOOL_URL")
    target_price = int(os.getenv("CORRECT_PRICE", "4800"))

    # State management
    wrong_price_count = 0
    alert_sent = False

    logging.info(f"Monitor active. Target: ${target_price}. Alert threshold: 5 mins.")

    while True:
        current_price = get_skool_price(url)

        if current_price is not None:
            if current_price != target_price:
                wrong_price_count += 1
                logging.warning(f"Price mismatch! Observed: ${current_price}. Strike {wrong_price_count}/5")
            else:
                if wrong_price_count > 0:
                    logging.info("Price returned to normal. Resetting counter.")
                wrong_price_count = 0
                alert_sent = False # Reset so we can alert again if it breaks later

        # Logic: If wrong for 5 mins (5 checks)
        if wrong_price_count >= 5 and not alert_sent:
            logging.critical("PRICE HAS BEEN WRONG FOR 5 MINUTES. TRIGGERING ALERT...")
            # We will build the send_slack function in the next step
            # For now, we just log it.
            alert_sent = True

        time.sleep(60) # Wait 60 seconds before next check

if __name__ == "__main__":
    main()
