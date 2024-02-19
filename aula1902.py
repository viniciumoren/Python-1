import os 

fah = int(input('Digite o valor em fahrenheit:'))

os.system('cls')

celsius = (fah-32)*5/9

print(f'O valor em Celsius é {celsius:.0f} °C')