cont=0
bandera=True
acumu=' '
print("Ingrese el texto en el documento: ")
while bandera:
    contenido=input()
    acumu=acumu+"\n"+contenido
    if contenido.endswith('.'):
        bandera=False
            
with open("palabras2.txt", 'w') as file:
    try:
        file.write(acumu.lstrip())
        print("modificacion exitosa")
        print('*****************************')
    except:
        print("Modificacion falló")

with open("palabras2.txt",'r') as file:
    lineas=file.read()

    with open("palabras2.txt", 'r') as file2:
        conLineas=0
        for i in file2 :
            conLineas=conLineas+1
    
cantidadCarac=len(lineas)

print("La cantidad de lineas es: %d\nLa cantidad de caractereses: %d\n\n"%(conLineas,cantidadCarac))

print('*'*len(lineas.split('\n')[0]))
print(lineas)
print('*'*len(lineas.split('\n')[0]))