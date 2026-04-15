# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
uv sync

# Run the monitor
uv run app/monitor.py

# Test Slack webhook connectivity
uv run app/test_slack.py
```

## Configuration

Copy `env.example` to `.env` and set:

- `SKOOL_URL` — the community's public `/about` page
- `CORRECT_PRICE` — expected price in whole USD dollars (e.g. `4800`)
- `ALERT_THRESHOLD` — number of consecutive failed checks before alerting (default: 5)
- `SLACK_WEBHOOK_URL` — Slack Incoming Webhook URL

## Architecture

The app is a polling loop that scrapes a Skool community page and alerts via Slack when the price deviates.

- `app/monitor.py` — entry point; 10-second polling loop with strike counter and alert-sent flag to prevent duplicate alerts
- `app/scraper.py` — fetches the page and extracts price from the `__NEXT_DATA__` Next.js JSON payload embedded in the HTML; Skool stores prices in cents (divide by 100)
- `app/notifier.py` — sends a Slack Block Kit message via webhook; reads env vars at call time