"""Leer una palabra diferente a fin y convertirla en mayuscula"""

palabra = input("Escribe una paplabra: ")

for i in range(10000000):
    if(palabra.lower()== "fin"):
        break
    else:
        print(f"{palabra.upper()} tiene {len(palabra)} letras")
        palabra = input("Escribe una palabra: ")
