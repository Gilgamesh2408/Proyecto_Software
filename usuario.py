from actividad import Actividad
class Usuario:
    def __init__(self, id, nombre, contraseña):
        self.id = id
        self.nombre = nombre
        self.contraseña = contraseña
        self.act = []

    def crear_actividad(self, nombre, fecha_inicio, fecha_final, descripcion, prioridad_tipo):
        # Crear una nueva instancia de Actividad y agregarla a la lista de actividades
        nueva_actividad = Actividad(nombre, fecha_inicio, fecha_final, descripcion, prioridad_tipo)
        self.act.append(nueva_actividad)

    def actualizar_actividad(self, indice, nombre, fecha_inicio, fecha_final, descripcion, prioridad_tipo):
        # Actualizar la actividad en el índice especificado
        if indice >= 0 and indice < len(self.act):
            self.act[indice].nombre = nombre
            self.act[indice].fecha_inicio = fecha_inicio
            self.act[indice].fecha_final = fecha_final
            self.act[indice].descripcion = descripcion
            self.act[indice].prioridad.tipo = prioridad_tipo
        else:
            print("Índice de actividad no válido")

    def eliminar_actividad(self, indice):
        # Eliminar la actividad en el índice especificado
        if indice >= 0 and indice < len(self.act):
            del self.act[indice]
        else:
            print("Índice de actividad no válido")