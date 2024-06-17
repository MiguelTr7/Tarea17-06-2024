import Funciones_Def as funcion
import time
#Creamos un menu de 4 opciones 
Cargos = ["CEO" , "Desarollador" , "ANALista de datos"]
while True:
    print ("1.- Registrar trabajador")
    print ("2.- Listar todos los trabajdores")
    print ("3.- Imprimir planillas del sueldo")
    print ("4.- Salir del programa")
    try:
        opc = input ("-> ")
    except ValueError:#mensaje de error 
        print ("Ingrese un caracter del 1 al 4")
    else:
        if opc == "1":
         funcion.registro();
         print ("")
        elif opc == "2":
            print ("")
        elif opc == "3":
            print ("")
        elif opc == "4":
            print ("")
        else: 
            print ("Ingrese un caracter del 1 al 4")
            time.sleep(2)
            print ("..")