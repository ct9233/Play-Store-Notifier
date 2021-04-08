import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from google_play_scraper import app
from twilio.rest import Client
from app_data import apps

load_dotenv("C:/data/.env")
account_sid = os.getenv("TWI_ACC_SID")
auth_token = os.getenv("TWI_AUTH_TOK")
twilio_from = os.getenv("TWI_FROM_NUM")
twilio_to = os.getenv("TWI_TO_NUM")

yesterday_timestamp = datetime.timestamp(datetime.now() - timedelta(days=1))
notification_message = ''

for key, val in apps.items():
    result = app(
        val,
        lang='en',
        country='us'
    )

    if result['free'] == True:
        notification_message = f"{key} is now free on the Google Play Store!"
    elif result['sale'] == True:
        notification_message = f"{key} is on sale on the Google Play Store for ${result['price']} until {datetime.fromtimestamp(result['saleTime'])}."
    elif result['updated'] > yesterday_timestamp:
        notification_message = f"{key} version has changed to {result['version']} on the Google Play Store.\nChanges: {result['recentChanges']}"

    if notification_message != '':
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=notification_message,
            from_=f"{twilio_from}",
            to=f"{twilio_to}"
        )