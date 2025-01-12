print("hello world")

msg=1

if msg==1:
    print("adios")
    
diccionario={}
diccionario[0]=1
diccionario[1]=2
diccionario={'1':2,'2':3}
diccionario[2]=8
print(diccionario)
palabra = 'brontosaurio'
d = dict()
for c in palabra:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
    print(d)