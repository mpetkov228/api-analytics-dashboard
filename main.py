from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

locations: list[dict] = [
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


@app.get("/", include_in_schema=False)
@app.get("/locations", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"locations": locations})


@app.get("/api/locations")
def get_locations():
    return locations