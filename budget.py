import string as str
import random as rd
from xmlrpc.client import boolean
"""
Password generator
"""
StringOrd = list(str.ascii_letters)
Numerico = list(str.digits)
StringEsp = list("<>!@_-#$%^&*()")
chara = list( str.ascii_letters+ str.digits +"<>!@_-#$%^&*()")


def generadorContra():
    Max = int(input("¿Cual es la cantidad de caracteres maximo de tu contraseña?"))
    min = int(input("¿Cual es la cantidad de caracteres minimo de tu contraseña?"))
    stop = True
    Contrasena = []
    Contra = ""
    i = int
    i = -1
    while stop:
        i = i + 1
        
        if(i < min):
            a = rd.randint(0,2)
            
            if(a == 0):
                b = rd.randint(0,1)
                if(b == 0):
                    Contrasena.append(rd.choice(StringOrd).lower())
                elif(b == 1):
                    Contrasena.append(rd.choice(StringOrd).upper())

            elif(a == 1):
                Contrasena.append(rd.choice(Numerico))
            elif(a == 2):
                Contrasena.append(rd.choice(StringEsp))
                 
        elif(i > min and i <= Max):
            a = rd.randint(0,4)
            if(a == 0):
                Contrasena.append(rd.choice(StringOrd))
            elif(a == 1):
                 Contrasena.append(rd.choice(Numerico))
            elif(a == 2):
                 Contrasena.append(rd.choice(StringEsp))
            elif(a== 4):
                stop = False
                return Contrasena
        elif(i > Max):
         stop = False
         return Contrasena