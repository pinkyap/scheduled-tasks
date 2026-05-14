import os
import requests
from twilio.rest import Client


 
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

#https://api.openweathermap.org/data/2.5/forecast?lat=19.0144&lon=72.8479&appid=93a6c13180b568fe82bcb517c273ae32

#lodz
#lat 51.759050
#long 19.458600

#mumbai
# "lat":19.0144,
# "lon":72.8479,
#it will decide
weather_params = {
    "lat":51.759050,
    "lon":19.458600,
    "appid":api_key,
    "cnt":4

}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
data = response.json()

bring_umbrella = False
#id = data["list"][3]["weather"][0]["id"]
id_list = []
for n in range(0,4):
    print(n)
    id = data["list"][n]["weather"][0]["id"]
    id_list.append(id)
    if id  == 500:
        bring_umbrella = True


#trial number +19789069714
if bring_umbrella:
    print("bring umbrellas")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="its going to rain today so bring your umbrella☔️",
        from_="+19789069714",
        to="+917039893483",
    )

print(message.status)


