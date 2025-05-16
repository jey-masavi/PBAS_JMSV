import os
import re
import base64
import csv
import json
import time
from dotenv import load_dotenv
from requests import post, get

class SpotifyAPI:
    def __init__(self):
        load_dotenv()
        self.client_id = os.getenv("CLIENT_ID")
        self.client_secret = os.getenv("CLIENT_SECRET")
        self.token = self.get_token()

    def get_token(self):
        auth_string = f"{self.client_id}:{self.client_secret}"
        auth_bytes = auth_string.encode("utf-8")
        auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

        url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": f"Basic {auth_base64}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {"grant_type": "client_credentials"}
        result = post(url, headers=headers, data=data)

        if result.status_code != 200:
            raise Exception("Error al obtener token.")

        return result.json()["access_token"]

    def get_auth_header(self):
        return {"Authorization": f"Bearer {self.token}"}

    def get_artists_by_genre(self, genre, limit_per_level=25):
        headers = self.get_auth_header()
        unique_artists = {}
        collected = {"alta": [], "media": [], "baja": []}
        offset = 0

        while any(len(collected[k]) < limit_per_level for k in collected) and offset < 1000:
            url = f"https://api.spotify.com/v1/search?q=genre:%22{genre}%22&type=artist&limit=50&offset={offset}"
            result = get(url, headers=headers)
            if result.status_code != 200:
                break
            artists = result.json().get("artists", {}).get("items", [])
            if not artists:
                break

            for artist in artists:
                pop = artist.get('popularity', 0)
                if pop >= 70 and len(collected["alta"]) < limit_per_level:
                    collected["alta"].append(artist)
                elif 40 <= pop < 70 and len(collected["media"]) < limit_per_level:
                    collected["media"].append(artist)
                elif pop < 40 and len(collected["baja"]) < limit_per_level:
                    collected["baja"].append(artist)

                if all(len(collected[k]) >= limit_per_level for k in collected):
                    break

            offset += 50
            time.sleep(0.2)

        for artist in collected['alta'] + collected['media'] + collected['baja']:
            artist_id = artist['id']
            if artist_id not in unique_artists:
                unique_artists[artist_id] = {
                    'artist_id': artist_id,
                    'name': artist['name'],
                    'genres': ','.join(artist['genres']) if artist['genres'] else 'Otros',
                    'popularity': artist['popularity'],
                    'followers': artist['followers']['total'],
                    'spotify_url': artist['external_urls']['spotify']
                }
        return unique_artists

    def get_songs_by_artist(self, artist_id, max_songs=5):
        url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=MX"
        headers = self.get_auth_header()
        result = get(url, headers=headers)
        tracks = result.json().get("tracks", [])[:max_songs]
        return [{
            'artist_id': artist_id,
            'song_name': t['name'],
            'song_url': t['external_urls']['spotify']
        } for t in tracks]

def save_csv(data, filename, fieldnames):
    os.makedirs("PIA", exist_ok=True)
    filepath = os.path.join("PIA", filename)
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"✓ Archivo guardado: {filepath}")

def menu():
    api = SpotifyAPI()
    all_artists = {}
    all_songs = []

    genres = [
        'rock', 'pop', 'hip hop', 'indie', 'electronic',
        'r&b', 'k-pop', 'jazz', 'reggaeton', 'classical'
    ]

    print("\n--- CONSULTA MUSICAL SPOTIFY ---")
    print("Géneros disponibles:")
    for i, g in enumerate(genres, 1):
        print(f"{i}. {g}")

    choices = input("\nSelecciona los géneros que deseas consultar (ej: 1,3,5): ")
    indices = [int(x.strip()) - 1 for x in choices.split(",") if x.strip().isdigit()]
    selected_genres = [genres[i] for i in indices if 0 <= i < len(genres)]

    if not selected_genres:
        print("No se seleccionaron géneros válidos.")
        return

    print("\nRecolectando artistas y canciones, espera...")

    for genre in selected_genres:
        artists = api.get_artists_by_genre(genre)
        all_artists.update(artists)
        songs = []
        for aid in artists:
            songs.extend(api.get_songs_by_artist(aid))
        all_songs.extend(songs)

    save_csv(
        list(all_artists.values()),
        "artists.csv",
        ['artist_id', 'name', 'genres', 'popularity', 'followers', 'spotify_url']
    )
    save_csv(
        all_songs,
        "popular_songs.csv",
        ['artist_id', 'song_name', 'song_url']
    )

    print("\n✓ Datos recopilados exitosamente.")

if __name__ == "__main__":
    menu()
