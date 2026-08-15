from fastapi import FastAPI, Request, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

locations: list[dict] = [
    { 
        "id": 'tokyo', 
        "name": 'Tokyo', 
        "country": 'Japan', 
        "temp": 24, 
        "cond": 'partly', 
        "hi": 27, 
        "lo": 19, 
        "feels": 25, 
        "humidity": 58, 
        "wind": 14, 
        "windDir": 'NE', 
        "pressure": 1013, 
        "visibility": 10, 
        "uv": 5, 
        "aqi": 42, 
        "sunrise": '5:12 AM', 
        "sunset": '6:48 PM' 
    },
    {
        "id": 'reykjavik', 
        "name": 'Reykjavík', 
        "country": 'Iceland', 
        "temp": 9, 
        "cond": 'rain', 
        "hi": 11, 
        "lo": 6, 
        "feels": 6, 
        "humidity": 82, 
        "wind": 28, 
        "windDir": 'W', 
        "pressure": 998, 
        "visibility": 6, 
        "uv": 1, 
        "aqi": 14, 
        "sunrise": '5:02 AM', 
        "sunset": '9:41 PM' 
    },
]


@app.get("/", include_in_schema=False)
@app.get("/locations", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"locations": locations})


@app.get("/saved", include_in_schema=False)
def saved(request: Request):
    return templates.TemplateResponse(request, "saved.html")


@app.get("/locations/{location_id}", include_in_schema=False)
def location_page(request: Request, location_id: str):
    for location in locations:
        if location.get("id") == location_id:
            title = f"{location["name"]}, {location["country"]} Weather"
            return templates.TemplateResponse(
                request, 
                "location.html", 
                {"location": location, "title": title}
            )

    return {"message": "Location not found"}


@app.get("/api/locations")
def get_locations():
    return locations


@app.get("/api/locations/{location_id}")
def get_location(location_id: str):
    for location in locations:
        if location.get("id") == location_id:
            return location

    raise HTTPException(status.HTTP_404_NOT_FOUND, "Location not found")