while False:
    linea= input("> ")
    if linea[0]== "#":
        continue
    if linea == "fin":
        break
    print(linea)

print("terminado")
def cuenta(a,b):
    contador=0
    for letra in a:
        if b== letra:
            contador=contador+1
    print("La letra aparece %d veces" %contador)

cuenta("Ferrocarril", "r")
hola="Ferrocarril"

#print(hola.upper().strip())

print(hola.count("r"))

#dato="From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"

dato="hola mundo extrañ@debo_comer ahhhh"
posIn=dato.find("@")
posFin=dato.find(" ",posIn)
print(dato[posIn+1:posFin])
print(len(dato[posIn+1:posFin]))
print("Este es el indice encontrado: %d" %dato.find("@",0,18))
# name=input("Ingrese el nombre del archivo: ")
# man = open(name, 'w')
#lectura= man.read()
#print(man)
print("---------------------------------")
conta=0
""" for lineas in man:
    conta=conta+1 """
   # print(lineas)
#
print("Numero de lineas: %d"%conta)

#print("Tamaño de la lectura: %d"%len(lectura))

#print(lectura)
# rstrip: elimina los espacios en blanco a  la derecha

""" man.write("Hello darkness my old friend \n")
man.close() """


print("**************")

""" for i in [1,2,3,4,5]:
    if not i%2==0: 
        continue
    print(i) """
    
# repr: junta todo en una cadena los saltos de linea los representa como\

##############################


#range y len: len el número de elementos de la list



#La función list divide una cadena en letras individuales. Si quieres dividir una
#cadena en palabras, puedes utilizar el método split:
#join es el inverso de split. Este toma una lista de cadenas y concatena los
#elementos. join es un método de cadenas, así que tienes que invocarlo en el
#delimitador y pasar la lista como un parámetro:


lista= ['a','b','c','d','e','f','g']
print(lista)
def recortar(a):
    del a[0]
    del a[len(a)-1]

recortar(lista)
print(lista)

def recort(lista):
    b=lista[1:len(lista)-1]
    return b

print("*****************************")


print(lista)
print(recort(lista))
print(lista is recort(lista))
print(lista)
print(recort(lista))