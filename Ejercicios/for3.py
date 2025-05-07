"""Contar palabras en una frase"""

Frase = input("Escribe una frase: ")

for i in Frase:
    contador_palabras = len(Frase.split())
    print(f"Hay {contador_palabras} palabras en la frase ingresada", end=".")
    break
else:
        print("La frase n tiene palabras")
        