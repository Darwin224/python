class Planilla:
    def __init__(self, fecha_corte):
        self.fecha_corte = fecha_corte
        self.trabajadores = []

    def agregar_trabajador(self, trabajador):
        self.trabajadores.append(trabajador)

    def calcular_total_planilla(self):
        total = 0
        for trabajador in self.trabajadores:
            total += trabajador.calcular_salario_neto()
        return total

    def generar_reporte(self):
        print("Reporte de Planilla")
        print(f"Fecha de corte: {self.fecha_corte}")
        print("=================================")
        for trabajador in self.trabajadores:
            print(f"Nombre: {trabajador.nombre} {trabajador.apellido}")
            print(f"ID: {trabajador.id}")
            print(f"Salario neto: {trabajador.calcular_salario_neto()}")
            print("------------------------------")
        print(f"Total planilla: {self.calcular_total_planilla()}")