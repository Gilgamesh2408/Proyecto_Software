from fecha import Fecha
from prioridad import Prioridad
class Actividad:
    def __init__(self, nombre, fecha_ini, fecha_fin, descripcion, priori, estado):
        self.nombre = nombre
        self.fecha_ini = Fecha(fecha_ini)  #Fecha
        self.fecha_fin = Fecha(fecha_fin)  #Fecha
        self.descripcion = descripcion
        self.priori = Prioridad(priori)    #Prioridad
        self.estado = estado

    def __str__(self):
        return f"Actividad: {self.nombre}\nFecha de inicio: {self.fecha_ini}\nFecha final: {self.fecha_fin}\nDescripción: {self.descripcion}\nPrioridad: {self.priori}\nEstado: {self.estado}"