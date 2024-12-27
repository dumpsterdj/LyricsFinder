from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from cover_img import fetch_itunes_metadata
from fastapi.staticfiles import StaticFiles
import requests

# Lyrics.ovh API base URL
LYRICS_OVH_API_BASE = "https://api.lyrics.ovh/v1"

# Initialize FastAPI app
app = FastAPI()

# Templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Function to fetch lyrics
def fetch_lyrics(artist: str, song: str):
    try:
        response = requests.get(f"{LYRICS_OVH_API_BASE}/{artist}/{song}")
        if response.status_code == 200:
            data = response.json()
            return data.get("lyrics", None)
        return None
    except Exception as e:
        print("Error fetching lyrics:", e)
        return None

# Home route
@app.get("/", response_class=HTMLResponse)
def home(request: HTMLResponse):
    return templates.TemplateResponse("home.html", {"request": {}})

# Search lyrics route
# @app.post("/search", response_class=HTMLResponse)
# async def search_lyrics(request: HTMLResponse, artist: str = Form(...), song: str = Form(...)):
#     print(f"Searching lyrics for artist: {artist}, song: {song}")  # Debugging
#     # lyrics = fetch_lyrics(artist, song)
#     # cover_image_url = fetch_cover_image(artist, song)
#     # if lyrics:
#     #     return templates.TemplateResponse("lyrics.html", {"request": {}, "lyrics": lyrics, "cover_image_url": cover_image_url})
#     # return templates.TemplateResponse("lyrics.html", {"request": {}, "error": "Lyrics not found. Please try again."})
#     lyrics = fetch_lyrics(artist, song)  # Fetch lyrics
#     metadata = fetch_itunes_metadata(artist, song)  # Fetch metadata from iTunes
#
#     return templates.TemplateResponse("lyrics.html", {
#         "request": None,
#         "lyrics": lyrics,
#         "cover_image_url": metadata.get("cover_image_url", ""),
#         "album": metadata.get("album", "Unknown Album"),
#         "release_date": metadata.get("release_date", "Unknown Date"),
#         "genre": metadata.get("genre", "Unknown Genre"),
#         "preview_url": metadata.get("preview_url", None)
#     })

@app.post("/search", response_class=HTMLResponse)
async def search_lyrics(artist: str = Form(...), song: str = Form(...)):
    lyrics = fetch_lyrics(artist, song)  # Fetch lyrics
    metadata = fetch_itunes_metadata(artist, song)  # Fetch metadata

    return templates.TemplateResponse("lyrics.html", {
        "request": None,
        "lyrics": lyrics,
        "cover_image_url": metadata.get("cover_image_url", ""),
        "album": metadata.get("album", "Unknown Album"),
        "release_date": metadata.get("release_date", "Unknown Date"),
        "genre": metadata.get("genre", "Unknown Genre"),
        "preview_url": metadata.get("preview_url", None)
    })