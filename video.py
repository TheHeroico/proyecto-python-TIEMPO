import time
import os
from datetime import datetime
#import winsound

def limpScreen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def aplicacion():
    funcion = input("presione 1 para saber la hora, 2 para empezar una cuenta regresiva, 3 para cronómetro, 4 para contador, 5 para marcador de dos equipos, 6 para metrónomo\n")
    limpScreen()
    if funcion == "1":
        horaActual()
    elif funcion == "2":
        cuentaAtras()
    elif funcion == "3":
        cronometro()
    elif funcion == "4":
        contador()
    elif funcion == "5":
        marcadorDosEquipos()
    elif funcion == "6":
        metronomo()
    

def horaActual():
    while botonHora == True:
        hora = datetime.now().time()
        #datetime.now().time() muestra la hora actual,
        #usando la clase datetime importada.
        limpScreen()
        print(hora)
        time.sleep(1)

def cuentaAtras():
    inicio = abs(int((input("Ingrese el tiempo en segundos\n"))))
    while inicio > 0:
        m, s = divmod(inicio, 60)
        h, m = divmod(m, 60)
        #The divmod() function returns a tuple containing the quotient 
        #and the remainder when argument1 (divident) is divided by argument2 (divisor).
        #6 / 60 = 0.1 residuo = 0
        tiempoRestante = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
        #Python zfill() is an inbuilt python string method that is used to 
        #append zero to the left side of the given string.
        limpScreen()
        print(tiempoRestante)
        time.sleep(1)
        inicio -= 1
        
def cronometro():
    for h in range (24):
        for m in range (60):
            for s in range (60):
                tiempo = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
                
                limpScreen()
                print(tiempo)
                time.sleep(1)
                
def contador():
    cont = 0
    print("Presione + para agregar 1, - para restar 1 y espacio para ver el total actual\n")
    while botonContador == True:
        
        n = str(input())
        if n == '+':
            cont = cont+1
            limpScreen()
            print(" El contador va en : " ,cont)
            
        elif n == '-':
            cont = cont-1
            limpScreen()
            print(" El contador va en : " ,cont)
            

def marcadorDosEquipos():
    botonreset1 = 0
    botonreset2 = 0
    marcador1 = 0
    marcador2 = 0
    print("Instrucciones:\n1 para aumentar un punto\n-1 para disminuir un punto\n2 para pasar \n0 es reiniciar el puntaje del jugador\n")
    
    while botonreset1 == 0 and botonreset2 == 0:
        
        decision1=int(input("Equipo 1:\n"))
        
        if decision1 == 1:
            marcador1 = marcador1 + 1
        elif decision1 == -1:
            marcador1 = marcador1 - 1
        elif decision1 == 0:
            marcador1 = 0
        elif decision1 == 2:
            pass
        limpScreen()
        print("El equipo 1 lleva: ", marcador1)
        print("El equipo 2 lleva: ", marcador2,"\n")
        
        decision2 = int(input("Equipo 2:\n"))
        
        if decision2 == 1:
            marcador2 = marcador2 + 1
        elif decision2 == -1:
            marcador2 = marcador2 - 1
        elif decision2 == 0:
            marcador2 = 0
        elif decision2 == 2:
            pass
        limpScreen()
        print("El equipo 1 lleva: ", marcador1)
        print("El equipo 2 lleva: ", marcador2,"\n")

def metronomo():
    duracionIntervalo = 60 / abs(int(input("Ingrese la velocidad en bpm (beats per minute)\n")))
    i = 0
    
    while True:
        print(i)
        i = i + 1
        time.sleep(duracionIntervalo)
        #winsound.PlaySound("*", winsound.SND_ALIAS)
        limpScreen()
        

botonHora = True
botonContador = True
aplicacion()
input()
