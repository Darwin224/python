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

class Actividad:
    pass
    # Implementación de la clase Actividad

class Planilla:
   pass
    # Implementación de la clase Planilla

class Deduccion:
    pass
    # Implementación de la clase Deduccion

class LoginSystem:
    pass
    # Implementación de la clase LoginSystem




class LoginSystem:
    # Resto de la implementación...

    def menu_trabajador(self, trabajador):
        while True:
            print("\nBienvenido,", trabajador.nombre)
            print("1. Ver información personal")
            print("2. Agregar actividad")
            print("3. Registrar horas trabajadas")
            print("4. Agregar deducción")
            print("5. Añadir nuevo trabajador")
            # Otras opciones del menú...

            opcion = int(input("\nSeleccione una opción: "))
            if opcion == 1:
                # Mostrar información personal del trabajador
                trabajador.imprimir_informacion()
            elif opcion == 2:
                # Recolectar datos y agregar actividad al trabajador
                costo = float(input("Ingrese el costo de la actividad: "))
                fecha_inicio = input("Ingrese la fecha de inicio: ")
                fecha_finalizacion = input("Ingrese la fecha de finalización: ")
                actividad = Actividad(costo, fecha_inicio, fecha_finalizacion)
                trabajador.agregar_actividad(actividad)
            elif opcion == 3:
                # Recolectar datos y registrar horas trabajadas
                horas = float(input("Ingrese las horas trabajadas: "))
                costo_por_hora = float(input("Ingrese el costo por hora: "))
                trabajador.registrar_horas_trabajadas(horas, costo_por_hora)
            elif opcion == 4:
                # Recolectar datos y agregar deducción al trabajador
                nombre_deduccion = input("Ingrese el nombre de la deducción: ")
                monto_deduccion = float(input("Ingrese el monto de la deducción: "))
                deduccion = Deduccion(nombre_deduccion, monto_deduccion)
                trabajador.agregar_deduccion(deduccion)
            elif opcion == 5:
                nuevo_trabajador = self.registrar_nuevo_trabajador()
                if nuevo_trabajador:
                    print("\n\t\tTrabajador registrado con éxito.\n")
            # Otras acciones según el menú...

    def registrar_nuevo_trabajador(self):
        # Recolectar datos del nuevo trabajador
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        id = input("ID: ")
        salario = float(input("Salario: "))
        cargo = input("Cargo: ")
        contraseña = input("Contraseña: ")

        nuevo_trabajador = Trabajador(id, nombre, apellido, salario, cargo, contraseña)
        # Agregar el nuevo trabajador a la lista de trabajadores en la clase o donde corresponda
        self.trabajadores.append(nuevo_trabajador)
        return nuevo_trabajador
