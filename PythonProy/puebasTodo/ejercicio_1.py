""" 
Ejercicio 1: Escribe un programa en Python que solicite al usuario ingresar cadena donde puede existir varias palabras. 
El programa debe tomar esas palabras, almacenarlas en una lista y luego convertir la lista en una tupla.
Luego, el programa debe generar un diccionario donde las palabras sean las claves y las repeticiones de las palabras sean los valores correspondientes. 
Por último, el programa debe guardar el diccionario en un archivo de texto llamado "palabras.txt". 
El programa debe diferenciar si el texto contiene caracteres que no sean letra (coma, punto, punto y coma, etc.) y omitirlos. """






texto=input("Ingresa una cadena de texto: ")
letrasLimpias = ""
#Validando con los metodos isalpha e isspace de la documentacion de str
#que la lista solo contenga letras 
for letras in texto:
    if letras.isalpha() or letras.isspace():
        letrasLimpias += letras


#creando la lista de palabras haciendo que todo se minuscula como estandar
palabras = letrasLimpias.lower().split()
palabrasTupla = tuple(palabras)
diccionario = {}

#Se asignan las palbras de la tupla a el diccionario y se valida la cantidad de veces
#que una palabra se repite
for palabraDicci in palabrasTupla:
    if palabraDicci in diccionario:
        diccionario[palabraDicci] += 1
    else:
        diccionario[palabraDicci] = 1

with open("palabras.txt", "w") as archivo:
    #convierte el diccionario en una cadena de texto
    archivo.write(str(diccionario))

print("El diccionario se ha guardado en el archivo 'palabras.txt'.")