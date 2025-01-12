# class trabajador:
#      def __init__(self, nombre, id, salario, contraseña,cargo):
#         self.nombre = nombre
#         self.id = id
#         self.salario = salario
#         self.contraseña = contraseña
#         self.cargo = cargo  

    
class Trabajador:
    def __init__(self, id, nombre, apellido, salario, cargo, contraseña, registrado_por):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario
        self.cargo = cargo
        self.contraseña = contraseña
        self.registrado_por = registrado_por
        self.actividades = []
        self.horas_trabajadas = []
        self.deducciones = []

    def agregar_actividad(self, actividad):
        self.actividades.append(actividad)

    def registrar_horas_trabajadas(self, horas, costo_por_hora):
        self.horas_trabajadas.append((horas, costo_por_hora))

    def agregar_deduccion(self, deduccion):
        self.deducciones.append(deduccion)

    def calcular_salario_neto(self):
        salario_bruto = self.salario

        for actividad in self.actividades:
            salario_bruto += actividad.costo

        for horas, costo_por_hora in self.horas_trabajadas:
            salario_bruto += horas * costo_por_hora

        for deduccion in self.deducciones:
            salario_bruto -= deduccion.monto

        return salario_bruto      