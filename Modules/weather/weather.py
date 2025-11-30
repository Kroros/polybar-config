#!/usr/bin/env python3


import requests, json
import os
from dotenv import load_dotenv, dotenv_values


icons = {
    "01d": "",
    "01n": "",
    "02d": "",
    "02n": "",
    "03d": "",
    "03n": "",
    "04d": "",
    "04n": "",
    "09d": "",
    "09n": "",
    "10d": "",
    "10n": "",
    "11d": "",
    "11n": "",
    "13d": "",
    "13n": "",
    "50d": "",
    "50n": "",
}

therm = ""

load_dotenv()

key = os.getenv("WEATHER_KEY")
lat = os.getenv("LAT")
lng = os.getenv("LNG")

weatherUrl = "https://api.openweathermap.org/data/2.5/weather?"
fullWeatherUrl = weatherUrl + "lat=" + lat + "&lon=" + lng + "&appid=" + key

weatherResponse = requests.get(fullWeatherUrl).json()

temp = 99
weather = "none"
icon= icons.get("01d")
if weatherResponse["cod"] != "404":
    temp = int(weatherResponse["main"]["temp"] -273)
    weather = weatherResponse["weather"][0]["main"]
    icoCode = weatherResponse["weather"][0]["icon"]
    icon = icons.get(icoCode)

print(f"{therm} {temp}°C {icon}")