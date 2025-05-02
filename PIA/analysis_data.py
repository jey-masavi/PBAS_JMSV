import csv
import re
import os
import json
from collections import defaultdict
from statistics import mean, median, mode, stdev, StatisticsError
import numpy as np

# Lista de géneros musicales válidos (palabras clave)
GENRES_VALIDOS = [
    'rock', 'pop', 'hip hop', 'indie', 'electronic',
    'r&b', 'k-pop', 'jazz', 'reggaeton', 'classical'
]

# Rutas a los archivos de entrada y salida
FOLDER = "PIA"
ARTISTS_FILE = os.path.join(FOLDER, "artists.csv")
SONGS_FILE = os.path.join(FOLDER, "popular_songs.csv")
CSV_OUTPUT_FILE = os.path.join(FOLDER, "resumen_por_genero.csv")
JSON_OUTPUT_FILE = os.path.join(FOLDER, "resumen_por_genero.json")

# ----- FUNCIONES DE VALIDACIÓN -----
# Verifica que la URL de Spotify tenga formato correcto
def validar_url(url):
    return re.match(r'^https:\/\/open\.spotify\.com\/.+$', url)

# Verifica que el nombre solo contenga caracteres válidos
def validar_nombre(nombre):
    return re.match(r"^[\w\s'&\-\.\(\)]+$", nombre)

# Valida que la cadena de géneros contenga solo letras y caracteres permitidos
def validar_generos(genre_string):
    return all(re.match(r'^[a-zA-Z\-& ]+$', g.strip()) for g in genre_string.split(','))

# Detecta el génerp principal entre varios, comparando con la lista de válidos
def detectar_genero_principal(generos_artista):
    for g in generos_artista:
        for clave in GENRES_VALIDOS:
            if clave.lower() in g.lower():
                return clave
    return 'Otros'

# ----- LECTURA Y LIMPIEZA DE DATOS -----
# Lee los artistas del archivo CSV y aplica validaciones
def leer_artistas():
    artistas = []
    with open(ARTISTS_FILE, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            generos = row['genres'].split(',')
            if (validar_url(row['spotify_url']) and
                validar_nombre(row['name']) and
                validar_generos(row['genres'])):

                genero_detectado = detectar_genero_principal(generos)

                artistas.append({
                    'id': row['artist_id'],
                    'name': row['name'],
                    'genres': [genero_detectado], # solo el género principal
                    'popularity': int(row['popularity']),
                    'followers': int(row['followers']),
                    'url': row['spotify_url']
                })
    return artistas

# Lee las canciones válidas (aunque no se analizan aún)
def leer_canciones():
    canciones = []
    with open(SONGS_FILE, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if validar_url(row['song_url']) and validar_nombre(row['song_name']):
                canciones.append(row)
    return canciones

# Calcula y muestra métricas estadísticas sobre popularidad y seguidores
def analizar_artistas(artistas):
    popularidades = [a['popularity'] for a in artistas]
    seguidores = [a['followers'] for a in artistas]

    print("\n----- Estadísticas de Popularidad: -----")
    print(f"Media: {mean(popularidades):.2f}")
    print(f"Mediana: {median(popularidades)}")
    try:
        print(f"Moda: {mode(popularidades)}")
    except StatisticsError:
        print("Moda: No única")
    print(f"Desviación estándar: {stdev(popularidades):.2f}")

    print("\n----- Estadísticas de Seguidores: -----")
    print(f"Media: {mean(seguidores):,.0f}")
    print(f"Mediana: {median(seguidores):,.0f}")
    try:
        print(f"Moda: {mode(seguidores):,}")
    except StatisticsError:
        print("Moda: No única")
    print(f"Desviación estándar: {stdev(seguidores):,.0f}")

# ----- AGRUPACIÓN POR GÉNERO Y EXPORTACIÓN -----
# Agrupa los artistas por género y calcula estadísticas por grupo
def preparar_datos_visualizacion(artistas):
    por_genero = defaultdict(list)
    for artist in artistas:
        genero = artist['genres'][0]
        por_genero[genero].append(artist['popularity'])

    resumen = []
    for genero, pops in por_genero.items():
        if len(pops) >= 3: #Solo se consideran géneros con 3+ artistas
            resumen.append({
                'género': genero,
                'cantidad_artistas': len(pops),
                'popularidad_media': round(np.mean(pops), 2),
                'popularidad_máxima': max(pops),
                'popularidad_mínima': min(pops)
            })
    return resumen

# Exporta el resumen a un archivo CSV
def exportar_resumen_csv(resumen):
    with open(CSV_OUTPUT_FILE, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['género', 'cantidad_artistas', 'popularidad_media', 'popularidad_máxima', 'popularidad_mínima']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(resumen)
    print(f"\nResumen por género exportado a: {CSV_OUTPUT_FILE}")

# Exporta el resumen a un archivo JSON
def exportar_resumen_json(resumen):
    with open(JSON_OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(resumen, f, ensure_ascii=False, indent=2)
    print(f"Resumen por género exportado también a JSON: {JSON_OUTPUT_FILE}")

# Ejecución principal
def main():
    artistas = leer_artistas()
    canciones = leer_canciones()

    print(f"\n✓ Artistas válidos leídos: {len(artistas)}")
    print(f"✓ Canciones válidas leídas: {len(canciones)}")

    analizar_artistas(artistas)
    resumen_genero = preparar_datos_visualizacion(artistas)

    print("\n----- Resumen por género: -----")
    for r in resumen_genero:
        print(f"- {r['género'].title()}: {r}")

    exportar_resumen_csv(resumen_genero)
    exportar_resumen_json(resumen_genero)

if __name__ == "__main__":
    main()