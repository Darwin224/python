class Trabajador:
    def __init__(self, id, nombre, apellido, salario, cargo, contraseña):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario
        self.cargo = cargo
        self.contraseña = contraseña
        self.actividades = []
        self.horas_trabajadas = []
        self.deducciones = []

    # Métodos para agregar actividades, horas trabajadas, deducciones, etc.


class Actividad:
    def __init__(self, costo, fecha_inicio, fecha_finalizacion):
        self.costo = costo
        self.fecha_inicio = fecha_inicio
        self.fecha_finalizacion = fecha_finalizacion


class Planilla:
    def __init__(self, fecha_corte):
        self.fecha_corte = fecha_corte
        self.trabajadores = []

    # Métodos para calcular valores y generar informes.


class Deduccion:
    def __init__(self, nombre, monto):
        self.nombre = nombre
        self.monto = monto


class LoginSystem:
    def __init__(self):
        self.trabajadores = []

    # Métodos para iniciar sesión, registrar empleados, mostrar menú, etc.


if __name__ == "__main__":
    login_system = LoginSystem()
    # Iniciar sesión y acceder al menú
