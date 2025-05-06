"""Leer ima palabra diferente a fin y convertirla a mayuscula"""

palabra = input("Escribe una palabra: ")
while palabra.lower() != "fin":
    print(palabra.upper())
    palabra = input("Escribe una palabra: ")
else: print("Ádios")