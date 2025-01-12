class Persona:
    def __init__(self, nombre, apellido, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.vida=100
   
    def saludar(self, nombre, apellido):
        print("Hola y bienvendio seas {} {}".format(nombre,apellido))
    
    def registrar (self, cedula: int ):
        print("Su numero de cedula es: {}".format(cedula))

    def datos(self):
        print("******************")
        print("Nombre:{}\nApellido: {}\nCedula: {}\n vida: {}".format(
            self.nombre,self.apellido,self.cedula,self.vida
        )) 
    
    def present(self, persona1):
        print("Hola {}, mi nombre es: {}".format(
            persona1,self.nombre
        ))

