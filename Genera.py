import random 
import os
from secrets import choice
import string 

def gen():
    nombre = str(input("Nombre de achivo"))
    ruta = os.getcwd()
    new_rute = ruta + "/" + nombre + ".txt"
    print("LA RUTA ES", new_rute)
    documento = open(new_rute, 'w')
    ingresa = int(input("Cantidad de lineas"))
    lista_ala=[]
    for i in range(ingresa):
        lista_ala.append(i) 
    for j,i in enumerate(lista_ala):
        
            documento.write(str(random.randint(0, 5000)) + " " +  str(random.choice(string.ascii_letters)) +" " + str(random.randint(0, 5000))+ " " + str(random.randint(0, 5000)) + os.linesep)
       
gen()  