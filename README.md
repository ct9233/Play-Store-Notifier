# Play-Store-Notifier

App to check for price and version changes on a Google Play Store app page and send text notification results

## Technologies
Project created with:

Python version: 3.9.0

## Setup
Running `python main.py` will execute the app

App expects `app_data.py` file in its root directory containing a dictionary named `apps` with entries in the format:
|key         |value          |
|------------|---------------|
|App Name    |App ID         |


## Dependencies
[Google-Play-Scraper](https://github.com/JoMingyu/google-play-scraper)

[Twilio API](https://www.twilio.com/docs/usage/api)
