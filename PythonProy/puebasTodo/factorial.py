valor=950

def factorial(a):
    
    if a==0:
        a=1
        return 1
    else:
        a=a*factorial(a-1)
        return a
    
print(factorial(valor))
numeros= str(factorial(valor))
i=0
print("\nLa cantidad de digitos es:")
for cont in numeros:
    i=i+1


print(i)