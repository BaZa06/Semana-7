"""Factorial de un número"""

número = int(input("Ingrese un número positivo: "))

while número < 0:
    print("El número debe ser positivo")
    número = int(input("Ingrese un número positivo: "))

factorial =1
for i in range(1, número + 1):
    factorial *= i

print(f"El factorial de {número} es {factorial}")