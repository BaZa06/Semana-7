"""Productos de los primeros M números pares"""

M = int(input("Ingrese un número positivo: "))

while M < 0:
    print("El número debe ser positivo")
    M = int(input("Ingrese un número positivo: "))
else:
    producto = 1
for i in range (1, M + 1):
    producto*= i * 2
print(f"El producto de los primeros {M} números pares es: {producto}")
    
 
