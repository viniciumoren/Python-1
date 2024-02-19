numeros = [5, -3, 10, 8, -2, 15, 7,-9, 5, 6]

positivos=[]
negativos=[]


for x in numeros:
    if x > 0 :
        positivos.append(x)

for x in numeros:
    if x < 0:
        negativos.append(x)

somaPositivos= sum(positivos)
somaNegativos= sum(negativos)


print (f'Positivos:{positivos}')
print (f'Negativos:{negativos}')

print (f'Soma de positivos:{somaPositivos}')
print (f'Soma de negativos:{somaNegativos}')
