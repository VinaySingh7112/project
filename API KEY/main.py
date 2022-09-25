import requests
from twilio.rest import Client

MY_LAT=24.793810
MY_LON=81.683990

link="https://api.openweathermap.org/data/2.5/onecall"

account_sid="ACb7a2921d47e6683752c9df5ad1a8296b"
auth_token="f751e98470ed80534a8cd7dfd6c918ef"

api_key="616c8165c0fdda3e4fe209241cf86799"

weather_parameters={
    "lat":MY_LAT,
    "lon":MY_LON,
    "appid":api_key,
    "exclude":"current,minutely,daily"

}

response=requests.get(link,params=weather_parameters)
response.raise_for_status()
weather_data=response.json()
weather_slice=weather_data["hourly"][:12]

will_rain=False
for hour_data in weather_slice:
    condition_code= hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain=True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
                body="It's going to rain today . Remember to bring an ☂️ ",
                from_="+19893598741",
                to="+916267597112",
             )

    print(message.status)