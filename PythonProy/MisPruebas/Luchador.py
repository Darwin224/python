from Persona import Persona


class Luchador(Persona):
      def __init__(self, nombre, apellido, cedula, fuerza):
            super().__init__(nombre, apellido, cedula)
            self.fuerza = fuerza

      def datos(self):
            super().datos()
            print("Fuerza: {}".format(self.fuerza))
      def pelear(self, persona):
            persona.vida=persona.vida- self.fuerza