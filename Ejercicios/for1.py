"""La suma de N números"""

número = int(input("Ingrese un número positivo:"))

for i in range(1, número+1):
    número += i
    print(f"La suma del 1 al {número}, es {número}")