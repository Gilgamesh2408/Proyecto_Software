class Fecha:
    def __init__(self, dia, mes, año, hora, minuto):
        self.dia = dia
        self.mes = mes
        self.año = año
        self.hora = hora
        self.minuto = minuto

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.año} {self.hora}:{self.minuto}"