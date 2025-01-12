class Actividad:
    def __init__(self, descripcion, costo, fecha_inicio, fecha_finalizacion):
        self.descripcion = descripcion
        self.costo = costo
        self.fecha_inicio = fecha_inicio
        self.fecha_finalizacion = fecha_finalizacion

    def calcular_duracion(self):
        duracion = self.fecha_finalizacion - self.fecha_inicio
        return duracion.days

    def mostrar_informacion(self):
        print("Información de la Actividad")
        print(f"Descripción: {self.descripcion}")
        print(f"Costo: {self.costo}")
        print(f"Fecha de inicio: {self.fecha_inicio}")
        print(f"Fecha de finalización: {self.fecha_finalizacion}")
        print(f"Duración: {self.calcular_duracion()} días")