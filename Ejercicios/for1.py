"""La suma de N números"""

número = int(input("Ingrese un número positivo:"))
suma = 0

for i in range(1, número+1):
    if número < 0:
        suma += i
        return suma
    print(f"La suma del 1 al {número} = {suma}.")
    break
else:
    print("El número no es positivo")
    número = int(input("Ingrese un número positivo: "))
