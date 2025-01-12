import Persona
import Luchador
name="juan"
apellido="Hernandez"
cedula=815

name2="lucas"
apellido2="barto"
cedula2=816
name3="Misterio"
apellido3="Rey"
cedula3=817
p= Persona.Persona(name,apellido,cedula)
p2=Persona.Persona(name2,apellido2,cedula2)
p3= Luchador.Luchador(name3, apellido3,cedula3,25)
p4 = Luchador.Luchador("ReyJr","Rodrigues",159,25)

p.saludar(p.nombre,p.apellido)
p.saludar(p2.nombre,p2.apellido)
p.saludar(p3.nombre,p3.apellido) 

p.present(p2.nombre)
p2.present(p.nombre)
p.present(p3.nombre)
p3.present(p.nombre)
p3.pelear(p2)
p4.pelear(p3)


p.datos()
p2.datos()
p3.datos()
p4.datos()


