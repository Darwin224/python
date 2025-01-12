
class Registro:
    def __init__(self):
        self.trabajadores = {}
    
    def registrar_trabajador(self, trabajador):
        self.trabajadores[trabajador.id] = trabajador
        print("\n\t\tTrabajador registrado con éxito.\n")
    
    def mostrar_trabajadores(self):
        print("Lista de trabajadores registrados:")
        for id_trabajador, trabajador in self.trabajadores.items():
            print(f"ID: {id_trabajador}, Nombre: {trabajador.nombre}, Cargo: {trabajador.cargo}, Salario: {trabajador.salario}")
    
    def autenticar_usuario(self, id_usuario, contraseña):
        if id_usuario in self.trabajadores and self.trabajadores[id_usuario].contraseña == contraseña:
            print("\n\t\t\tAutenticación exitosa. ¡Bienvenido!")
            return True
        else:
            print("\n\t\t¡¡¡Error de autenticación!!! Por favor, verifica tus credenciales.")
            return False
    
    def imprimir_informacion_trabajador(self, id_trabajador):
        if id_trabajador in self.trabajadores:
            trabajador = self.trabajadores[id_trabajador]
            print("Información del Trabajador:")
            print(f"Nombre: {trabajador.nombre}")
            print(f"ID: {trabajador.id}")
            print(f"Cargo: {trabajador.cargo}")
            print(f"Salario: {trabajador.salario}")
            print(f"Contraseña: {trabajador.contraseña}")
        else:
            print("Trabajador no encontrado.")


    
