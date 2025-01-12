""" 	Registro o inicio de sesión: En él se llevará a cabo una condicional, si el usuario es un maestro de obra podrá hacer modificaciones, como añadir obrero, eliminar obrero o cambiar su salario como se especifica arriba
•	Atributos:
1.	Nombre de usuario
2.	Cargo
3.	Contraseña
 """
import registro
import trabajador as tr
import planilla
maestros_registrados=[]
trabajadores_registrados = []
registro = registro.Registro()

print("Calculadora de planilla\n", "*******************************************")
while True:
    print("Opciones:")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")
    try:
        opcion = int(input("\nSeleccione una opción: "))
        print("*"*12)
    except ValueError:
        print("Ingresa un numero valido")
        continue

    if opcion == 1:
        print("Ingrese sus datos\n")
        nombre = input("Nombre:")
        apellido = input("Apellido:")
        id = input("Id:")
        salario = input("Salario:")
        cargo = input("Cargo:")
        contraseña = input("Contraseñá:")
        newtrabajador = tr.trabajador(
            nombre=nombre, id=id, salario=salario, contraseña=contraseña, cargo=cargo)
        maestros_registrados.append(newtrabajador)
        registro.registrar_trabajador(newtrabajador)

    elif opcion == 2:
        print("\nIniciar Sesion")
        print("*"*12)
        usuario = input("Ingrese su nombre de usuario (id): ")
        contraseña = input("Ingrese su nombre de Contraseña: ")
        ValidarUsuario = registro.autenticar_usuario(usuario, contraseña)
        print("\n"*2)

        if ValidarUsuario == True:
            # cargo = newtrabajador.cargo
            cargo = None
            for trabajador in maestros_registrados:
                if trabajador.id == usuario:
                    cargo = trabajador.cargo

            if cargo == "maestro":
                print("\t\tBienvenido\n")
                print("\t\tnMenú")
                print("1. Añadir obreros")
                print("2. Asignar dias trabajados")
                print("3. Calcular planilla")
                print("4. Modificar Salario")
                print("5. Eliminar obreros")
                opcionM = int(input("Seleccione una opcion"))

                if opcionM == 1:
                    print("Ingrese sus datos\n")
                    nombre = input("Nombre:")
                    apellido = input("Apellido:")
                    id = input("Id:")
                    salario = input("Salario:")
                    cargo = input("Cargo:")
                    contraseña = input("Contraseñá:")
                    newtrabajador = tr.trabajador(
                        nombre=nombre, id=id, salario=salario, contraseña=contraseña, cargo=cargo)
                    trabajadores_registrados.append(newtrabajador)
                    registro.registrar_trabajador(newtrabajador)

                elif opcionM == 4:
                    userT = input("ingrese el usuario del trabajador: ")
                    sal = input("Ingrese el salario")
                    for trabajador in trabajadores_registrados:
                        if trabajador.id == userT:
                            trabajador.salario = sal
                            registro.imprimir_informacion_trabajador(
                                trabajador.id)
                          # newtrabajador.setSalario(usuario==userT,salario=sal)
                elif opcionM == 5:
                    for tbj in trabajadores_registrados:
                        registro.imprimir_informacion_trabajador(tbj.id)

            elif cargo == "obrero":
                print("Soy obrero")

    elif opcion == 3:
        print("Saliendo...")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
print("Fin del programa")
