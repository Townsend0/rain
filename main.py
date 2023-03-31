import requests
from twilio.rest import Client
import os

a = requests.get("https://api.openweathermap.org/data/3.0/onecall?lat=38.4237&lon=27.1428&exclude=current&appid=8585e4aa7dc338316aeca9512c9b6312")
for b in range(14):
    if a.json()["hourly"][b]["weather"][0]["id"] < 700:
        a = Client(os.environ.get("wt1"), os.environ.get("wt2"))
        a.messages.create(from_=f'whatsapp:{os.environ.get("wts")}',body='its gonna rain tomorrow',to=f'whatsapp:{os.environ.get("wtsm")}')
        break
