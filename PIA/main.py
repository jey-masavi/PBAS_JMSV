from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
import re

# Cargar credenciales
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

    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

# Encabezado de autenticación
def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

# Validar nombre de artista
def is_valid_artist_name(name):
    return bool(re.match(r"^[a-zA-ZÀ-ÿ\s.'-]{2,50}$", name.strip()))

# Buscar artista por nombre
def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]

    if len(json_result) == 0:
        print("No existe ningún artista con este nombre...")
        return None

    return json_result[0]

# Obtener canciones populares
def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

# Obtener álbumes
def get_albums_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/albums?include_groups=album,single&limit=10"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["items"]
    return json_result

# Menú principal
def menu():
    token = get_token()
    if not token:
        return

    artist_data = None

    # Función para solicitar un nuevo artista
    def solicitar_artista():
        nonlocal artist_data
        while True:
            artist_name = input("\nIntroduce el nombre del artista: ")
            if not is_valid_artist_name(artist_name):
                print("Nombre no válido. Usa solo letras, espacios y algunos símbolos básicos.")
                continue

            artist_data = search_for_artist(token, artist_name)
            if artist_data:
                print(f"\nArtista encontrado: {artist_data['name']}")
                break
            else:
                print("No se encontró el artista. Intenta con otro nombre.")

    # Pedir artista inicial
    solicitar_artista()

    # Menú interactivo
    while True:
        print("\n----- ¿QUÉ DESEAS CONSULTAR? -----")
        print("1. Información sobre el artista")
        print("2. Ver canciones populares del artista")
        print("3. Ver álbumes del artista")
        print("4. Buscar otro artista")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            print(f"\nInformación de {artist_data['name']}:")
            print(f"Géneros musicales: {', '.join(artist_data['genres']) if artist_data['genres'] else 'No especificados'}")
            print(f"Popularidad: {artist_data['popularity']}")
            print(f"Seguidores: {artist_data['followers']['total']:,}")
            print(f"Spotify URL: {artist_data['external_urls']['spotify']}")
            print(f"ID: {artist_data['id']}")

        elif opcion == '2':
            songs = get_songs_by_artist(token, artist_data['id'])
            print(f"\nCanciones populares de {artist_data['name']}:")
            for idx, song in enumerate(songs):
                print(f"{idx + 1}. {song['name']} (Popularidad: {song['popularity']})")

        elif opcion == '3':
            albums = get_albums_by_artist(token, artist_data['id'])
            print(f"\nÁlbumes y singles de {artist_data['name']}:")
            for idx, album in enumerate(albums):
                print(f"{idx + 1}. {album['name']} - {album['release_date']}")

        elif opcion == '4':
            solicitar_artista()  # Cambiar de artista

        elif opcion == '5':
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
