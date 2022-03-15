import requests
import json
import datetime

openweather_key = 'e9440b964702a7ff63bd26f7b08cf9b3'

location = 'asan'

def now_time():
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")
    return now


def get_weather():
    try:
        url = 'https://api.openweathermap.org/data/2.5/weather?q={0}&units=Metric&appid={1}'.format(location, openweather_key)
        res = requests.get(url)
        data = json.loads(res.text)

        weather = data['weather'][0]['main']
        temp = data['main']['temp']
        humi = data['main']['humidity']
        max_temp = data['main']['temp_max']
        min_temp = data['main']['temp_min']
        wind_speed = data['wind']['speed']
        wind_deg = data['wind']['deg']
        icon = data['weather'][0]['icon']

        packet = [
            now_time(),
            weather,
            temp,
            humi,
            max_temp,
            min_temp,
            wind_speed,
            wind_deg,
            icon
        ]

        print(packet)
        return packet

    except Exception as ex:
        print(ex)
