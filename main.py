import os
from dotenv import load_dotenv
from google_play_scraper import app
from twilio.rest import Client

account_sid = os.getenv("TWI_ACC_SID")
auth_token = os.getenv("TWI_AUTH_TOK")
twilio_from = os.getenv("TWI_FROM_NUM")
twilio_to = os.getenv("TWI_TO_NUM")

slay_spire_price = 9.99
slay_spire_version = "2.2.6"

result = app(
    'com.humble.SlayTheSpire',
    lang='en',
    country='us'
)

if result['price'] != slay_spire_price:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"The Google Play Store price for Slay the Spire has changed to {result['price']}.",
        from_=f"{twilio_from}",
        to=f"{twilio_to}"
    )
elif result['free'] == True:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Slay the Spire is now free on the Google Play Store!",
        from_=f"{twilio_from}",
        to=f"{twilio_to}"
    )
elif result['sale'] == True:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"Slay the Spire is on sale on the Google Play Store for ${result['price']} during {result['saleTime']}.",
        from_=f"{twilio_from}",
        to=f"{twilio_to}"
    )
elif result['version'] != slay_spire_version:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"Slay the Spire version has changed to {result['version']} on the Google Play Store.\nChanges: {result['recentChanges']}",
        from_=f"{twilio_from}",
        to=f"{twilio_to}"
    )
