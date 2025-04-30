from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
import csv
import time

# Cargar las variables de entorno desde .env
load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# Obtener token de acceso
def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)

    if result.status_code != 200:
        print("Error al obtener token de autenticación.")
        return None

    return result.json()["access_token"]

# Devuelve el header de autorización para usar en peticiones a la API
def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

# Obtiene hasta 10 canciones populares de un artista (limitado a 5 luego)
def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=MX"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    return result.json().get("tracks", [])

# Guarda los datos de artistas en CSV
def save_artists_csv(artistis_dict, filename="artists.csv"):
    folder = "PIA"
    os.makedirs(folder, exist_ok=True) # Crea la carpeta si no existe
    filepath = os.path.join(folder, filename)

    with open(filepath, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['artist_id', 'name', 'genres', 'popularity', 'followers', 'spotify_url']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(artistis_dict.values())

    print(f"\nArchivo de artistas guardado en: {filepath}")

# Guarda los datos de canciones en CSV
def save_songs_csv(songs, filename="popular_songs.csv"):
    folder = "PIA"
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, filename)

    with open(filepath, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['artist_id', 'song_name', 'song_url']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(songs)

    print(f"Archivo de canciones guardado en: {filepath}")

# Recolectar artistas únicos por género
def collect_artists(token, genres_to_search):
    headers = get_auth_header(token)
    unique_artists = {}

    for genre in genres_to_search:
        print(f"\nProcesando género: {genre}")
        collected = {"alta": [], "media": [], "baja": []}
        offset = 0

        while any(len(collected[k]) < 25 for k in collected) and offset < 1000:
            url = f"https://api.spotify.com/v1/search?q=genre:%22{genre}%22&type=artist&limit=50&offset={offset}"
            result = get(url, headers=headers)

            if result.status_code != 200:
                break

            artists = result.json().get("artists", {}).get("items", [])
            if not artists:
                break

            # Clasificar artistas según su popularidad
            for artist in artists:
                pop = artist.get('popularity', 0)
                if pop >= 70 and len(collected["alta"]) < 25:
                    collected["alta"].append(artist)
                elif 40 <= pop < 70 and len(collected["media"]) < 25:
                    collected["media"].append(artist)
                elif pop < 40 and len(collected["baja"]) < 25:
                    collected["baja"].append(artist)

                # Si ya se juntaron 25 por cada nivel, salir
                if all(len(collected[k]) >= 25 for k in collected):
                    break
            
            offset += 50
            time.sleep(0.2) # Esperar un poco para no sobrecargar la API

        # Agregar artistas únicos al diccionario
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
        print(f"✓ 75 artistas recopilados del género '{genre}'.")
    
    return unique_artists

# Recolectar canciones populares por artista
def collect_songs(token, artists_dict):
    songs_data = []
    for artist_id in artists_dict:
        songs = get_songs_by_artist(token, artist_id)[:5]
        for song in songs:
            songs_data.append({
                'artist_id': artist_id,
                'song_name': song['name'],
                'song_url': song['external_urls']['spotify']
            })
        time.sleep(0.2)
    return songs_data

# Función principal
def main():
    token = get_token()
    if not token:
        print("No se pudo obtener el token.")
        return
    
    # Género a procesar
    genres = ['rock', 'pop', 'hip hop', 'indie', 'electronic', 'r&b', 'k-pop', 'jazz', 'reggaeton', 'classical']
    artists = collect_artists(token, genres)
    songs = collect_songs(token, artists)
 
    # Guardar datos en archivos separados
    save_artists_csv(artists)
    save_songs_csv(songs)

# Ejecutar el script
if __name__ == "__main__":
    main()
