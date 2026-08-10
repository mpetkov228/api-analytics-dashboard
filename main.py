from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

locations: list = [
    {
        "id": 1,
        "name": "London",
        "temp": "21°c",
        "precip": "15%",
        "weather_phrase": "Cloudy"
    },
    {
        "id": 2,
        "name": "Burgas",
        "temp": "29°c",
        "precip": "0%",
        "weather_phrase": "Sunny"
    },
]


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/locations", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>Weather in {locations[0]["name"]} - {locations[0]["temp"]}</h1>"


@app.get("/api/locations")
def get_locations():
    return locations