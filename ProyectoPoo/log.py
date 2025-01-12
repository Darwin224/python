# import sqlite3

# class LoginSystem:
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
#                 contraseña TEXT,
#                 registrado_por TEXT
#             )
#         ''')
#         self.conn.commit()

#     # Resto de los métodos

#     def menu_trabajador(self, trabajador):
#         while True:
#             print("\nBienvenido,", trabajador[1])
#             print("1. Ver información personal")
#             print("2. Modificar salario")
#             print("3. Mostrar lista de trabajadores registrados por ti")
#             print("4. Eliminar cuenta")
#             print("5. Añadir trabajadores")
#             print("6. Salir")
  
#             try:
#                 opcion = int(input("\nSeleccione una opción: "))
#             except ValueError:
#                 print("Ingrese un número válido.")
#                 continue

#             if opcion == 1:
#                 self.imprimir_informacion_trabajador(trabajador[0])
#             elif opcion == 2:
#                 nuevo_salario = float(input("Ingrese el nuevo salario: "))
#                 self.cursor.execute('''
#                     UPDATE trabajadores
#                     SET salario = ?
#                     WHERE id = ? AND registrado_por = ?
#                 ''', (nuevo_salario, trabajador[0], trabajador[0]))
#                 self.conn.commit()
#                 print("Salario actualizado con éxito.")
#             elif opcion == 3:
#                 self.imprimir_lista_trabajadores(trabajador[0])
#             elif opcion == 4:
#                 confirmacion = input("¿Estás seguro de eliminar tu cuenta? (si/no): ")
#                 if confirmacion.lower() == "si":
#                     self.cursor.execute('''
#                         DELETE FROM trabajadores WHERE id = ? AND registrado_por = ?
#                     ''', (trabajador[0], trabajador[0]))
#                     self.conn.commit()
#                     print("Cuenta eliminada exitosamente.")
#                     break
           
#             elif opcion==5:
#                 nuevo_trabajador = self.registrar_nuevo_trabajador(trabajador[0])
#                 if nuevo_trabajador:
#                     print("\n\t\tTrabajador registrado con éxito.\n")

#             elif opcion == 6:
#                 print("Cerrando sesión...")
#                 break
#             else:
#                 print("Opción inválida. Seleccione una opción válida.")


#     def registrar_trabajador(self, trabajador):
#         self.cursor.execute('''
#             INSERT INTO trabajadores (id, nombre, apellido, salario, cargo, contraseña, registrado_por)
#             VALUES (?, ?, ?, ?, ?, ?, ?)
#         ''', (trabajador.id, trabajador.nombre, trabajador.apellido, trabajador.salario, trabajador.cargo, trabajador.contraseña, trabajador.id))
#         self.conn.commit()
#         print("\n\t\tTrabajador registrado con éxito.\n")

#     def registrar_nuevo_trabajador(self, user_id):
#         print("\nRegistro de nuevo trabajador:")
#         nombre = input("Nombre: ")
#         apellido = input("Apellido: ")
#         id = input("ID: ")
#         salario = float(input("Salario: "))
#         cargo = input("Cargo: ")
#         contraseña = input("Contraseña: ")

#         self.cursor.execute('''
#             INSERT INTO trabajadores (id, nombre, apellido, salario, cargo, contraseña, registrado_por)
#             VALUES (?, ?, ?, ?, ?, ?, ?)
#         ''', (id, nombre, apellido, salario, cargo, contraseña, user_id))
#         self.conn.commit()
#         return True
    

#     def imprimir_informacion_trabajador(self, id_trabajador):
#         trabajador = self.cursor.execute('''
#             SELECT * FROM trabajadores WHERE id = ?
#         ''', (id_trabajador,)).fetchone()

#         if trabajador is not None:
#             print("\nInformación del trabajador:")
#             print("Nombre:", trabajador[1])
#             print("ID:", trabajador[0])
#             print("Apellido:", trabajador[2])
#             print("Salario:", trabajador[3])
#             print("Cargo:", trabajador[4])
#             print("Contraseña:", trabajador[5])
#             print("Registrado por:", trabajador[6])  # Agregar esta línea
#         else:
#             print("No se encontró ningún trabajador con ese ID.")

#     def imprimir_lista_trabajadores(self, user_id):
#         trabajadores = self.cursor.execute('''
#             SELECT * FROM trabajadores WHERE registrado_por = ?
#         ''', (user_id,)).fetchall()

#         if trabajadores:
#             print("\nLista de trabajadores registrados por M  i:")
#             for trabajador in trabajadores:
#                 print("ID:", trabajador[0])
#                 print("Nombre:", trabajador[1])
#                 print("Apellido:", trabajador[2])
#                 print("Salario:", trabajador[3])
#                 print("Cargo:", trabajador[4])
#                 print("------------------------")
#         else:
#             print("No hay trabajadores registrados por ti.") 

            
#     def iniciar_sesion(self):
#         print("Calculadora de planilla\n", "*******************************************")
#         while True:
#             print("Opciones:")
#             print("1. Registrarse")
#             print("2. Iniciar sesión")
#             print("3. Salir")
#             try:
#                 opcion = int(input("\nSeleccione una opción: "))
#                 print("*" * 12)
#             except ValueError:
#                 print("Ingresa un numero valido")
#                 continue

#             if opcion == 1:
#                 print("Ingrese sus datos\n")
#                 nombre = input("Nombre:")
#                 apellido = input("Apellido:")
#                 id = input("Id:")
#                 salario = float(input("Salario:"))
#                 cargo = input("Cargo:")
#                 contraseña = input("Contraseñá:")

#                 self.cursor.execute('''
#                     INSERT INTO trabajadores (id, nombre, apellido, salario, cargo, contraseña)
#                     VALUES (?, ?, ?, ?, ?, ?)
#                 ''', (id, nombre, apellido, salario, cargo, contraseña))
#                 self.conn.commit()

#             elif opcion == 2:
#                 print("\nIniciar Sesion")
#                 print("*" * 12)
#                 usuario = input("Ingrese su nombre de usuario (id): ")
#                 contraseña = input("Ingrese su nombre de Contraseña: ")
#                 ValidarUsuario = self.cursor.execute('''
#                     SELECT * FROM trabajadores WHERE id = ? AND contraseña = ?
#                 ''', (usuario, contraseña)).fetchone()

#                 print("\n" * 2)

#                 if ValidarUsuario is not None:
#                         self.menu_trabajador(ValidarUsuario)

#                 else:
#                     print("Credenciales inválidas.")

#             elif opcion == 3:
#                 print("Saliendo...")
#                 break

#             else:
#                 print("Opción inválida. Por favor, seleccione una opción válida.")
#         print("Fin del programa")

import sqlite3

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

class Actividad:
    def __init__(self, costo, fecha_inicio, fecha_finalizacion):
        self.costo = costo
        self.fecha_inicio = fecha_inicio
        self.fecha_finalizacion = fecha_finalizacion

class Deduccion:
    def __init__(self, descripcion, monto):
        self.descripcion = descripcion
        self.monto = monto

class LoginSystem:
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
                contraseña TEXT,
                registrado_por TEXT
            )
        ''')
        self.conn.commit()

    # Resto de los métodos

    def menu_trabajador(self, trabajador):
        while True:
            print("\nBienvenido: ,", trabajador[1])
            print("1. Mi informacion personal")
            print("2. Añadir trabajadores")
            print("3. Modificar salario")
            print("4. Mi equipo")
            print("5. Eliminar cuenta")
            print("6. Salir")
  
            try:
                opcion = int(input("\nSeleccione una opción: "))
            except ValueError:
                print("Ingrese un número válido.")
                continue

            if opcion == 1:
                self.imprimir_informacion_trabajador(trabajador[0])

            elif opcion==2:
                nuevo_trabajador = self.registrar_nuevo_trabajador(trabajador[0])
                if nuevo_trabajador:
                    print("\n\t\tTrabajador registrado con éxito.\n")

            elif opcion == 3:
                nuevo_salario = float(input("Ingrese el nuevo salario: "))
                self.cursor.execute('''
                    UPDATE trabajadores
                    SET salario = ?
                    WHERE id = ? AND registrado_por = ?
                ''', (nuevo_salario, trabajador[0], trabajador[0]))
                self.conn.commit()
                print("Salario actualizado con éxito.")

            elif opcion == 4:
                self.imprimir_lista_trabajadores(trabajador[0])

            elif opcion == 5:
                confirmacion = input("¿Estás seguro de eliminar tu cuenta? (si/no): ")
                if confirmacion.lower() == "si":
                    self.cursor.execute('''
                        DELETE FROM trabajadores WHERE id = ? AND registrado_por = ?
                    ''', (trabajador[0], trabajador[0]))
                    self.conn.commit()
                    print("Cuenta eliminada exitosamente.")
                    break
           
            elif opcion == 6:
                print("Cerrando sesión...")
                break
            else:
                print("Opción inválida. Seleccione una opción válida.")


    def registrar_trabajador(self, trabajador):
        self.cursor.execute('''
            INSERT INTO trabajadores (id, nombre, apellido, salario, cargo, contraseña, registrado_por)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (trabajador.id, trabajador.nombre, trabajador.apellido, trabajador.salario, trabajador.cargo, trabajador.contraseña, trabajador.id))
        self.conn.commit()
        print("\n\t\tTrabajador registrado con éxito.\n")

    def registrar_nuevo_trabajador(self, user_id):
        print("\nRegistro de nuevo trabajador:")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        id = input("ID: ")
        salario = float(input("Salario: "))
        cargo = input("Cargo: ")
        contraseña = input("Contraseña: ")

        self.cursor.execute('''
            INSERT INTO trabajadores (id, nombre, apellido, salario, cargo, contraseña, registrado_por)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (id, nombre, apellido, salario, cargo, contraseña, user_id))
        self.conn.commit()
        return True
    

    def imprimir_informacion_trabajador(self, id_trabajador):
        trabajador = self.cursor.execute('''
            SELECT * FROM trabajadores WHERE id = ?
        ''', (id_trabajador,)).fetchone()

        if trabajador is not None:
            print("\nInformación del trabajador:")
            print("Nombre:", trabajador[1])
            print("ID:", trabajador[0])
            print("Apellido:", trabajador[2])
            print("Salario:", trabajador[3])
            print("Cargo:", trabajador[4])
            print("Contraseña:", trabajador[5])
            print("Registrado por:", trabajador[6])  # Agregar esta línea
        else:
            print("No se encontró ningún trabajador con ese ID.")

    def imprimir_lista_trabajadores(self, user_id):
        trabajadores = self.cursor.execute('''
            SELECT * FROM trabajadores WHERE registrado_por = ?
        ''', (user_id,)).fetchall()

        if trabajadores:
            print("\nLista de trabajadores registrados por M  i:")
            for trabajador in trabajadores:
                print("ID:", trabajador[0])
                print("Nombre:", trabajador[1])
                print("Apellido:", trabajador[2])
                print("Salario:", trabajador[3])
                print("Cargo:", trabajador[4])
                print("------------------------")
        else:
            print("No hay trabajadores registrados por ti.") 

            
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


if __name__ == "__main__":
    login_system = LoginSystem()
    login_system.iniciar_sesion()
   

