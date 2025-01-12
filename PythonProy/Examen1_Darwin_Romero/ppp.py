class MiClase:
    def __init__(self):
        self.conteo = 0
        MiClase.conteo += 1

a = MiClase()
print(a.conteo) # 0
b = MiClase()
print(b.conteo) # 0
c = MiClase()
print(c.conteo) # 0
a.conteo