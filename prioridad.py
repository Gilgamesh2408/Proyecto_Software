class Prioridad:
    def __init__(self, tipo):
        self.tipo = tipo
        self.nombre, self.color = self.obtener_prioridad_y_color()

    def obtener_prioridad_y_color(self):
        if self.tipo == 1:
            return "Baja", "verde"
        elif self.tipo == 2:
            return "Media", "amarillo"
        elif self.tipo == 3:
            return "Alta", "naranja"
        elif self.tipo == 4:
            return "Urgente", "rojo"
        else:
            raise ValueError("Tipo de prioridad no válido")

    def __str__(self):
        return f"Prioridad: {self.nombre}\nColor: {self.color}"