import os
import sys
import csv
import json
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import Workbook
from openpyxl.drawing.image import Image as XLImage
from openpyxl.utils.dataframe import dataframe_to_rows
from statistics import mean, median, mode, stdev, StatisticsError
from collections import defaultdict

class AnalizadorSpotify:
    def __init__(self):
        self.folder = "PIA"
        self.artists_path = os.path.join(self.folder, "artists.csv")
        self.songs_path = os.path.join(self.folder, "popular_songs.csv")
        self.summary_path = os.path.join(self.folder, "resumen_por_genero.csv")
        self.json_path = os.path.join(self.folder, "resumen_por_genero.json")
        self.graphs_dir = os.path.join(self.folder, "Graficas")
        os.makedirs(self.graphs_dir, exist_ok=True)

    def validar_nombre(self, nombre):
        return bool(re.match(r"^[\w\s'&\-\.\(\)]+$", nombre))

    def validar_url(self, url):
        return url.startswith("https://open.spotify.com")

    def leer_artistas(self):
        artistas = []
        with open(self.artists_path, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if self.validar_url(row['spotify_url']) and self.validar_nombre(row['name']):
                    genero = self.detectar_genero_principal(row['genres'].split(','))
                    artistas.append({
                        'id': row['artist_id'],
                        'name': row['name'],
                        'genres': [genero],
                        'popularity': int(row['popularity']),
                        'followers': int(row['followers']),
                        'url': row['spotify_url']
                    })
        return artistas

    def detectar_genero_principal(self, generos):
        claves = ['rock', 'pop', 'hip hop', 'indie', 'electronic', 'r&b', 'k-pop', 'jazz', 'reggaeton', 'classical']
        for g in generos:
            for c in claves:
                if c.lower() in g.lower():
                    return c
        return "Otros"

    def analizar(self, artistas):
        resumen = defaultdict(list)

        for a in artistas:
            resumen[a['genres'][0]].append(a['popularity'])

        resultados = []
        for genero, pops in resumen.items():
            if len(pops) >= 3:
                resultados.append({
                    'género': genero,
                    'cantidad_artistas': len(pops),
                    'popularidad_media': round(np.mean(pops), 2),
                    'popularidad_máxima': max(pops),
                    'popularidad_mínima': min(pops)
                })

        with open(self.summary_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=resultados[0].keys())
            writer.writeheader()
            writer.writerows(resultados)

        with open(self.json_path, 'w', encoding='utf-8') as f:
            json.dump(resultados, f, indent=2, ensure_ascii=False)

        print("✓ Resumen generado y exportado.")

    def graficar(self):
        df = pd.read_csv(self.summary_path)
        ruta1 = self._guardar_grafica(df['género'], df['cantidad_artistas'], "Cantidad de Artistas", "barras_artistas.png")
        ruta2 = self._guardar_grafica(df['género'], df['popularidad_media'], "Popularidad Media", "linea_popularidad.png", tipo='linea')
        ruta3 = self._grafico_dispersion(df)
        ruta4 = self._grafico_pastel(df)

        # Mostrar todas las gráficas en pantalla
        plt.show()

        # Crear Excel con gráficas insertadas
        wb = Workbook()
        ws1 = wb.active
        ws1.title = "Resumen por género"
        for r in dataframe_to_rows(df, index=False, header=True):
            ws1.append(r)

        ws2 = wb.create_sheet("Gráficas")
        for i, path in enumerate([ruta1, ruta2, ruta3, ruta4]):
            img = XLImage(path)
            img.width, img.height = 500, 300
            ws2.add_image(img, f"A{1 + i * 20}")

        wb.save(os.path.join(self.folder, "visualizacion_spotify.xlsx"))
        print("✓ Archivo Excel generado con gráficas.")

    def _guardar_grafica(self, x, y, titulo, filename, tipo='barras'):
        fig, ax = plt.subplots()
        if tipo == 'linea':
            ax.plot(x, y, marker='o')
        else:
            ax.bar(x, y, color='skyblue')
        ax.set_title(titulo)
        ax.set_xlabel("Género")
        ax.set_ylabel(titulo)
        ruta = os.path.join(self.graphs_dir, filename)
        fig.savefig(ruta)

        # Mostrar la figura también
        fig.show()

        return ruta

    def _grafico_dispersion(self, df):
        fig, ax = plt.subplots()
        ax.scatter(df['popularidad_mínima'], df['popularidad_máxima'], color='purple')
        for _, row in df.iterrows():
            ax.annotate(row['género'], (row['popularidad_mínima'], row['popularidad_máxima']))
        ax.set_title("Dispersión Min vs Máx")
        ruta = os.path.join(self.graphs_dir, "dispersión_popularidad.png")
        fig.savefig(ruta)
        fig.show()
        return ruta

    def _grafico_pastel(self, df):
        fig, ax = plt.subplots()
        ax.pie(df['cantidad_artistas'], labels=df['género'], autopct='%1.1f%%')
        ax.set_title("Distribución por género")
        ruta = os.path.join(self.graphs_dir, "pastel_proporcion.png")
        fig.savefig(ruta)
        fig.show()
        return ruta

if __name__ == "__main__":
    analizador = AnalizadorSpotify()
    artistas = analizador.leer_artistas()
    analizador.analizar(artistas)
    analizador.graficar()
