"""Contador vocales en cadena"""

cadena = input("Escribe una palabra: ")

for i in cadena:
    if i.lower() in "aeiou":
        print(f"{i} es una vocal")
    else:
        print(f"{i} no es una vocal")
