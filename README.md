# Skool Price Monitor

### Functionality
This application monitors the price of a Skool community by scraping the site's underlying metadata.

* **Frequency:** Runs on a 60-second loop.
* **Logic:** If the price deviates from the target value for a set number of consecutive minutes, it triggers a Slack alert.
* **Alerting:** Sends a notification via Slack Webhook once the threshold is met.

---

### Prerequisites
* **Python 3.12+**
* **uv** (Environment manager)

---

### Installation

1. **Clone the repository** to the local machine or server.
2. **Create a `.env` file** in the root directory:
   ```text
   SKOOL_URL=[https://www.skool.com/your-community/about](https://www.skool.com/your-community/about)
   CORRECT_PRICE=29
   ALERT_THRESHOLD=5
   SLACK_WEBHOOK_URL=[https://hooks.slack.com/services/YOUR/WEBHOOK/HERE](https://hooks.slack.com/services/YOUR/WEBHOOK/HERE)
