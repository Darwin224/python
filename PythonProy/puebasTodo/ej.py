import string
text = input('Ingrese una cadena de texto: ')
with open("pal", 'w') as file:
   file.write(text)
with open("pal", 'r') as file:
   texto=file.readline()

counts =  dict()


for line in texto:
    line = line.rstrip()
    line = line.translate(line.maketrans("","",string.punctuation))
    line = line.lower()
    words = line.split(" ")
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
   




with open("palabrasNuevas.txt", "w") as archivo:
    #convierte el diccionario en una cadena de texto
    archivo.write(str(counts))

print("El diccionario se ha guardado en el archivo 'palabrasNuevas.txt'.")