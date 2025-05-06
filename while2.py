"""Leer una palabra e indicar su número de letras"""

palabra = input("Escribe una palabra: ")
while palabra.lower() != "fin":
    print(f"{palabra.upper()} tiene {len(palabra)} letras")
    palabra = input("Escribe una palabra: ")
else: print("Adiós...")