numeros = [12,22,23,24,34,35,36,77,88]

impar=[]

for x in numeros:
    if x%2==0:
        print(x)

    else:
        impar.append(x)

print(impar)