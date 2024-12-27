import requests

ITUNES_API_BASE = "https://itunes.apple.com/search"

def fetch_itunes_metadata(artist: str, song: str):
    query = f"{song} {artist}"
    response = requests.get(
        ITUNES_API_BASE,
        params={"term": query, "entity": "musicTrack", "limit": 1}
    )
    if response.status_code == 200:
        data = response.json()
        results = data.get("results", [])
        if results:
            song_info = results[0]
            metadata = {
                "cover_image_url": song_info.get("artworkUrl600", ""),
                "album": song_info.get("collectionName", "Unknown Album"),
                "release_date": song_info.get("releaseDate", "").split("T")[0],
                "genre": song_info.get("primaryGenreName", "Unknown Genre"),
                "preview_url": song_info.get("previewUrl", None)
            }
            print(metadata)  # Debugging: Check fetched metadata
            return metadata
        return {"error": "No matching song found."}
    return {"error": f"Error: {response.status_code}, {response.text}"}

if __name__ == "__main__":
    # Example usage for testing
    artist_name = input("Enter the artist name: ")
    song_title = input("Enter the song title: ")
    metadata = fetch_itunes_metadata(artist_name, song_title)
    print(metadata)
