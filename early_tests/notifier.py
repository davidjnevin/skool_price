import os
import requests
import logging

def send_slack_alert(current_price, target_price):
    url = os.getenv("SLACK_WEBHOOK_URL")
    threshold = os.getenv("ALERT_THRESHOLD")

    # We create a simple string message just like your --data '{"text":"..."}'
    alert_text = (
        f"🚨 *PRICE ALERT*: The Skool price is currently *${current_price}*.\n"
        f"It was expected to be ${target_price}."
    )

    # We use a professional "Block Kit" style message for Slack
    message = {
        "text": "🚨 PRICE ALERT",
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "🚨 Price Mismatch Detected"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Community:* {os.getenv('SKOOL_URL')}\n"
                           f"*Status:* Incorrect for {threshold} minutes."
                }
            },
            {
                "type": "fields",
                "fields": [
                    {"type": "mrkdwn", "text": f"*Expected:* ${target_price}"},
                    {"type": "mrkdwn", "text": f"*Observed:* ${current_price}"}
                ]
            }
        ]
    }

    payload = {"text": alert_text}

    try:
        # requests.post(..., json=payload) automatically sets the Content-type to application/json
        response = requests.post(url, json=payload, timeout=10)

        if response.status_code == 200:
            logging.info("Slack alert sent successfully.")
        else:
            logging.error(f"Slack returned an error: {response.status_code} - {response.text}")

    except Exception as e:
        logging.error(f"Failed to connect to Slack: {e}")


