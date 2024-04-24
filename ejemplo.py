import json
import time

# Lista de tareas pendientes
tareas_pendientes = []

# Función para cargar las tareas pendientes desde un archivo JSON
def cargar_tareas():
    try:
        with open("evento.json", "r") as file:
            tareas_pendientes.extend(json.load(file))
    except FileNotFoundError:
        pass

# Función para guardar las tareas pendientes en un archivo JSON
def guardar_tareas():
    with open("evento.json", "w") as file:
        json.dump(tareas_pendientes, file, indent=4)

# Función para añadir una tarea pendiente
def agregar_tarea(msg, subject, timestamp):
    tarea = {"msg": msg, "subject": subject, "timestamp": timestamp}
    tareas_pendientes.append(tarea)
    guardar_tareas()

# Función para revisar las tareas pendientes y imprimir los mensajes si el timestamp coincide en un rango de 5 segundos
def revisar_tareas():
    while True:
        for tarea in tareas_pendientes:
            if abs(time.time() - tarea["timestamp"]) <= 5:
                print(tarea["msg"])
                tareas_pendientes.remove(tarea)
                guardar_tareas()
        time.sleep(1)

# Cargar tareas pendientes existentes
cargar_tareas()

# Agregar una nueva tarea pendiente
agregar_tarea("Tarea 1", "Asunto 1", time.time() + 2)

# Iniciar el proceso de revisión de tareas
revisar_tareas()
