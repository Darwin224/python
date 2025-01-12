import registro
import trabajador as tr
import planilla
# import sqlite3
# class login:

#     def __init__(self):
#         self.conn = sqlite3.connect('trabajadores.db')
#         self.cursor = self.conn.cursor()
#         self.cursor.execute('''
#             CREATE TABLE IF NOT EXISTS trabajadores (
#                 id TEXT PRIMARY KEY,
#                 nombre TEXT,
#                 apellido TEXT,
#                 salario REAL,
#                 cargo TEXT,
#                 contraseña TEXT
#             )
#         ''')
#         self.conn.commit()
#     maestros_registrados=[]
#     trabajadores_registrados = []
#     def __init__(self) -> None:
        
#         self.registro = registro.Registro()

#     def iniciar_sesion(self):
        

#         print("Calculadora de planilla\n", "*******************************************")
#         while True:
#             print("Opciones:")
#             print("1. Registrarse")
#             print("2. Iniciar sesión")
#             print("3. Salir")
#             try:
#                 opcion = int(input("\nSeleccione una opción: "))
#                 print("*"*12)
#             except ValueError:
#                 print("Ingresa un numero valido")
#                 continue

#             if opcion == 1:
#                 print("Ingrese sus datos\n")
#                 nombre = input("Nombre:")
#                 apellido = input("Apellido:")
#                 id = input("Id:")
#                 salario = input("Salario:")
#                 cargo = input("Cargo:")
#                 contraseña = input("Contraseñá:")
#                 newtrabajador = tr.trabajador(
#                     nombre=nombre, id=id, salario=salario, contraseña=contraseña, cargo=cargo)
#                 login.maestros_registrados.append(newtrabajador)
#                 self.registro.registrar_trabajador(newtrabajador)
                
#             elif opcion == 2:
#                 print("\nIniciar Sesion")
#                 print("*"*12)
#                 usuario = input("Ingrese su nombre de usuario (id): ")
#                 contraseña = input("Ingrese su nombre de Contraseña: ")
#                 ValidarUsuario = self.registro.autenticar_usuario(usuario, contraseña)
#                 print("\n"*2)

#                 if ValidarUsuario == True:
#                     # cargo = newtrabajador.cargo
#                     cargo = None
#                     for trabajador in login.maestros_registrados:
#                         if trabajador.id == usuario:
#                             cargo = trabajador.cargo

#                     if cargo == "maestro":
#                         print("\t\tBienvenido\n")
#                         print("\t\tnMenú")
#                         print("1. Añadir obreros")
#                         print("2. Asignar dias trabajados")
#                         print("3. Calcular planilla")
#                         print("4. Modificar Salario")
#                         print("5. Eliminar obreros")
#                         opcionM = int(input("Seleccione una opcion"))

#                         if opcionM == 1:
#                             print("Ingrese sus datos\n")
#                             nombre = input("Nombre:")
#                             apellido = input("Apellido:")
#                             id = input("Id:")
#                             salario = input("Salario:")
#                             cargo = input("Cargo:")
#                             contraseña = input("Contraseñá:")
#                             newtrabajador = tr.trabajador(
#                                 nombre=nombre, id=id, salario=salario, contraseña=contraseña, cargo=cargo)
#                             login.trabajadores_registrados.append(newtrabajador)
#                             self.registro.registrar_trabajador(newtrabajador)

#                         elif opcionM == 4:
#                             userT = input("ingrese el usuario del trabajador: ")
#                             sal = input("Ingrese el salario")
#                             for trabajador in login.trabajadores_registrados:
#                                 if trabajador.id == userT:
#                                     trabajador.salario = sal
#                                     self.registro.imprimir_informacion_trabajador(
#                                         trabajador.id)
#                                 # newtrabajador.setSalario(usuario==userT,salario=sal)
#                         elif opcionM == 5:
#                             for tbj in login.trabajadores_registrados:
#                                 self.registro.imprimir_informacion_trabajador(tbj.id)

#                     elif cargo == "obrero":
#                         print("Soy obrero")

#             elif opcion == 3:
#                 print("Saliendo...")
#                 break

#             else:
#                 print("Opción inválida. Por favor, seleccione una opción válida.")
#         print("Fin del programa")

import sqlite3

class login:
     #   
    def __init__(self):
        self.conn = sqlite3.connect('trabajadores.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS trabajadores (
                id TEXT PRIMARY KEY,
                nombre TEXT,
                apellido TEXT,
                salario REAL,
                cargo TEXT,
                contraseña TEXT
            )
        ''')
        self.conn.commit()

    def menu_trabajador(self, trabajador):
        while True:
            print("\nBienvenido,", trabajador[1])
            print("1. Ver información personal")
            print("2. Modificar salario")
            print("3. Mostrar lista de trabajadores")
            print("4. Eliminar cuenta")
            print("5. Añadir trabajadores")
            print("6. Salir")

            try:
                opcion = int(input("\nSeleccione una opción: "))
            except ValueError:
                print("Ingrese un número válido.")
                continue

            if opcion == 1:
                self.imprimir_informacion_trabajador(trabajador[0])
            elif opcion == 2:
                nuevo_salario = float(input("Ingrese el nuevo salario: "))
                self.cursor.execute('''
                    UPDATE trabajadores
                    SET salario = ?
                    WHERE id = ?
                ''', (nuevo_salario, trabajador[0]))
                self.conn.commit()
                print("Salario actualizado con éxito.")
            elif opcion == 3:
                self.imprimir_lista_trabajadores()
            elif opcion == 4:
                confirmacion = input("¿Estás seguro de eliminar tu cuenta? (si/no): ")
                if confirmacion.lower() == "si":
                    self.cursor.execute('''
                        DELETE FROM trabajadores WHERE id = ?
                    ''', (trabajador[0],))
                    self.conn.commit()
                    print("Cuenta eliminada exitosamente.")
                    break
            elif opcion==5:
                self.registrar_nuevo_trabajador()
            elif opcion == 6:
                print("Cerrando sesión...")
                break
            else:
                print("Opción inválida. Seleccione una opción válida.")

    def registrar_nuevo_trabajador(self):
        print("\nRegistro de nuevo trabajador:")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        id = input("ID: ")
        salario = float(input("Salario: "))
        cargo = input("Cargo: ")
        contraseña = input("Contraseña: ")

        self.cursor.execute('''
            INSERT INTO trabajadores (id, nombre, apellido, salario, cargo, contraseña)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (id, nombre, apellido, salario, cargo, contraseña))
        self.conn.commit()
        print("Trabajador registrado con éxito.")

    def imprimir_informacion_trabajador(self, id):
        trabajador = self.cursor.execute('''
            SELECT * FROM trabajadores WHERE id = ?
        ''', (id,)).fetchone()

        if trabajador is not None:
            print("\nInformación del trabajador:")
            print("ID:", trabajador[0])
            print("Nombre:", trabajador[1])
            print("Apellido:", trabajador[2])
            print("Salario:", trabajador[3])
            print("Cargo:", trabajador[4])
            print("Contraseña:", trabajador[5])
        else:
            print("No se encontró ningún trabajador con ese ID.")

    def imprimir_lista_trabajadores(self):
        trabajadores = self.cursor.execute('''
            SELECT * FROM trabajadores
        ''').fetchall()

        if trabajadores:
            print("\nLista de trabajadores:")
            for trabajador in trabajadores:
                print("ID:", trabajador[0])
                print("Nombre:", trabajador[1])
                print("Apellido:", trabajador[2])
                print("Salario:", trabajador[3])
                print("Cargo:", trabajador[4])
                print("Contraseña:", trabajador[5])
                print("------------------------")
        else:
            print("No hay trabajadores registrados.")
    #

    def iniciar_sesion(self):
        print("Calculadora de planilla\n", "*******************************************")
        while True:
            print("Opciones:")
            print("1. Registrarse")
            print("2. Iniciar sesión")
            print("3. Salir")
            try:
                opcion = int(input("\nSeleccione una opción: "))
                print("*" * 12)
            except ValueError:
                print("Ingresa un numero valido")
                continue

            if opcion == 1:
                print("Ingrese sus datos\n")
                nombre = input("Nombre:")
                apellido = input("Apellido:")
                id = input("Id:")
                salario = float(input("Salario:"))
                cargo = input("Cargo:")
                contraseña = input("Contraseñá:")

                self.cursor.execute('''
                    INSERT INTO trabajadores (id, nombre, apellido, salario, cargo, contraseña)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (id, nombre, apellido, salario, cargo, contraseña))
                self.conn.commit()

            elif opcion == 2:
                print("\nIniciar Sesion")
                print("*" * 12)
                usuario = input("Ingrese su nombre de usuario (id): ")
                contraseña = input("Ingrese su nombre de Contraseña: ")
                ValidarUsuario = self.cursor.execute('''
                    SELECT * FROM trabajadores WHERE id = ? AND contraseña = ?
                ''', (usuario, contraseña)).fetchone()

                print("\n" * 2)

                if ValidarUsuario is not None:
                        self.menu_trabajador(ValidarUsuario)

                else:
                    print("Credenciales inválidas.")

            elif opcion == 3:
                print("Saliendo...")
                break

            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
        print("Fin del programa")


