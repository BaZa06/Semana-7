import datetime
import random
import time as t
import os

fecha = datetime.date.today()

print("Bienvenido /n{fecha}")

def esperar(espera):
    for i in range(espera):
        os.system("cls || clear")
        print(f"Espera {espera}")
        espera-=1
        t.sleep(1)
    os.system("cls || clear")

def adivinar(num_user, num_rdn, espera):
    if num_user == num_rdn:
        t.sleep(espera)
        print("Adivinaste")
    else:
        print("Lo siento, no es lo número")
        
def main():
    num_alea = random.randint(1,10)
    resp = "s"  
    while resp.lower() != 'n':
        num = input("Ingresa un número del 1 al 10: ")
        adivinar(int(num), num_alea)
        resp = input("¿Desea seguir jugando? [S = Si = N = No - R = Reiniciar partida]")
main()