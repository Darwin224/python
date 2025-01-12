#Ejercicio 2: Escribe un programa en Python que lea el archivo "palabras.txt" originado en el ejercicio anterior.
#El programa debe cargar el diccionario desde el archivo y luego calcular el promedio de las longitudes de las palabras en el diccionario 
#y mostrar la palabra o palabras más repetidas. 
#El resultado debe ser impreso en la pantalla.

# Leer el archivo y cargar el diccionario
with open("palabras.txt", "r") as file:
    diccionario = eval(file.read())

# Calcular el promedio de las longitudes de las palabras
totalPalabras = sum(diccionario.values())
totalLongitud = 0
for palabra, frecuencia in diccionario.items():
    longitudPalabra = len(palabra)
    totalLongitud += longitudPalabra * frecuencia

promedioLongitud = totalLongitud / totalPalabras
# imprimimos el resultado con dos decimales
print('************************************')
print("Promedio de longitud de palabras: {:.2f}".format(promedioLongitud))

maxFrecuencia = max(diccionario.values())
# Luego, creamos una lista de palabras que tienen la frecuencia máxima
palabrasMasRepetidas = []
for palabra, frecuencia in diccionario.items():
    if frecuencia == maxFrecuencia:
        palabrasMasRepetidas.append(palabra)

# las palabras más repetidas separadas por comas
print('**********************************')
print("Palabras más repetidas: {}".format(', '.join(palabrasMasRepetidas)))
