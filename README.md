# Skool Price Monitor

### Functionality
This application monitors the price of a Skool community by scraping the site's underlying metadata.

* **Frequency:** Runs on a 60-second loop.
* **Logic:** If the price deviates from the target value for a set number of consecutive minutes, it triggers a Slack alert.
* **Alerting:** Sends a formatted notification via Slack Webhook once the threshold is met.

---

### Prerequisites
* **Python 3.12+**
* **uv** (Python package and environment manager)

---

### Project Structure
```text
.
├── app/
│   ├── monitor.py     # Main monitoring loop and logic
│   ├── scraper.py     # JSON data extraction module
│   ├── notifier.py    # Slack Webhook integration
│   └── test_slack.py  # Connectivity test script
├── .env               # Local configuration (Private)
├── pyproject.toml     # Dependency definitions
└── uv.lock            # Version lockfile
```

## Installation
1. Clone the repository to the local machine or server.
1. Create a .env file in the root directory:

```Plaintext
SKOOL_URL=https://www.skool.com/your-community/about
CORRECT_PRICE=29
ALERT_THRESHOLD=5
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/HERE
```

### Initialize and sync the environment:
```python
Bash
uv sync
```

## Usage
### Start the monitor:
```python
Bash
uv run app/monitor.py
```

### Test Slack connectivity:
```python
Bash
uv run app/test_slack.py
```

### Configuration Details
SKOOL_URL: The public "About" page of the community.
CORRECT_PRICE: The numerical USD value the script expects.
ALERT_THRESHOLD: The number of minutes (checks) the price must remain incorrect before an alert is sent.
SLACK_WEBHOOK_URL: The Incoming Webhook URL generated from the Slack App directory.
