import tkinter as tk
from tkinter import messagebox
import subprocess
import threading
import os

class SpotifyAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Spotify Data Analyzer")
        self.root.geometry("400x450")
       
        # Géneros disponibles
        self.GENRES = [
            'rock', 'pop', 'hip hop', 'indie', 'electronic',
            'r&b', 'k-pop', 'jazz', 'reggaeton', 'classical'
        ]
       
        # Diccionario de checkbuttons
        self.checks = {}
       
        # Crear la interfaz
        self.crear_interfaz()

    def crear_interfaz(self):
        # Etiqueta de título
        tk.Label(self.root, text="Selecciona los géneros musicales:", font=("Arial", 12)).pack(pady=10)

        # Checkboxes para cada género
        for genero in self.GENRES:
            var = tk.BooleanVar()
            tk.Checkbutton(self.root, text=genero.title(), variable=var).pack(anchor="w", padx=20)
            self.checks[genero] = var

        # Botón para recolectar datos
        tk.Button(self.root, text="Recolectar datos", command=self.lanzar_consulta, bg="#85C1E9").pack(pady=20)

        # Botón para análisis y visualización
        tk.Button(self.root, text="Analizar y Visualizar", command=self.lanzar_analisis, bg="#82E0AA").pack(pady=10)

    # Función para ejecutar el script de consulta con géneros seleccionados
    def ejecutar_consulta_con_generos(self, generos_seleccionados):
        if not generos_seleccionados:
            messagebox.showwarning("Advertencia", "Selecciona al menos un género.")
            return

        # Ruta completa de script1.py
        script1_path = os.path.join("C:\\", "Users", "jesse", "OneDrive", "Documentos", "GitHub", "PBAS_JMSV", "PIA", "script1.py")
       
        # Llama al script con los géneros como argumento usando subprocess
        args = ["python", script1_path] + generos_seleccionados
        try:
            subprocess.run(args, check=True)
            messagebox.showinfo("Éxito", "Consulta finalizada.")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Ocurrió un error:\n{e}")

    # Función para ejecutar el análisis y visualización
    def ejecutar_analisis(self):
        # Ruta completa de script2.py
        script2_path = os.path.join("C:\\", "Users", "jesse", "OneDrive", "Documentos", "GitHub", "PBAS_JMSV", "PIA", "script2.py")
       
        try:
            subprocess.run(["python", script2_path], check=True)
            messagebox.showinfo("Éxito", "Análisis y visualización completados.")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Ocurrió un error:\n{e}")

    # Función para lanzar consulta en segundo plano
    def lanzar_consulta(self):
        # Obtener géneros seleccionados
        seleccionados = [g for g, var in self.checks.items() if var.get()]
       
        # Crear un hilo para ejecutar la consulta sin bloquear la interfaz
        threading.Thread(target=self.ejecutar_consulta_con_generos, args=(seleccionados,), daemon=True).start()

    # Función para lanzar análisis en segundo plano
    def lanzar_analisis(self):
        threading.Thread(target=self.ejecutar_analisis, daemon=True).start()


# Crear la ventana principal y la aplicación
root = tk.Tk()
app = SpotifyAnalyzerApp(root)
root.mainloop()