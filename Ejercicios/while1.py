"""Productos de los primeros M números pares"""

número = int(input("Ingrese un número positivo: "))

while número < 0:
    print("El número debe ser positivo")
    número = int(input("Ingrese un número positivo: "))
else:
    producto = 1
for i in range (1, número + 1):
    producto*= i * 2
print(f"El producto de los primeros {número} números pares es: {producto}")
    
 
