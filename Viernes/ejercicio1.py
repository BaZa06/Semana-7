#Leer un número y mostrar una lista del 1 hasta el número junto con su cuadrado si es positivo y par

numero = int(input("Escriba un número positivo: "))
resultado = 0

for i in range (1, numero + 1):
    resultado = i**2 
    print(f"El conteo del 1 al {numero}, es igual a: {resultado}")
    if numero > 0:
     print("Es positivo")
    elif numero % 2 == 0:
     print("Es par")
else:
    print("Escriba un número par y positivo")