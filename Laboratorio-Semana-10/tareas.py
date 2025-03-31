# tareas.py (módulo)

# Clase Tarea (para paradigma orientado a objetos)
class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False
    
    def marcar_completada(self):
        self.completada = True
    
    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - {estado}"

# Función para mostrar todas las tareas (paradigma estructurado)
def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas en la lista.")
    for tarea in tareas:
        print(tarea)

# Función para agregar una nueva tarea (paradigma estructurado)
def agregar_tarea(tareas, descripcion):
    tarea = Tarea(descripcion)
    tareas.append(tarea)

# Función para eliminar una tarea (paradigma estructurado)
def eliminar_tarea(tareas, descripcion):
    tarea_a_eliminar = next((tarea for tarea in tareas if tarea.descripcion == descripcion), None)
    if tarea_a_eliminar:
        tareas.remove(tarea_a_eliminar)
        print(f"Tarea '{descripcion}' eliminada.")
    else:
        print(f"No se encontró la tarea '{descripcion}'.")