import time
import

Cargos = ["CEO" , "Desarollador" , "ANALista de datos"]
while True:
    print ("1.- Registrar trabajador")
    print ("2.- Listar todos los trabajdores")
    print ("3.- Imprimir planillas del sueldo")
    print ("4.- Salir del programa")
    try:
        opc = input ("-> ")
    except ValueError:
        print ("Ingrese un caracter del 1 al 4")
    else:
        if opc == "1":
            print (1)
        elif opc == "2":
            print (2)
        elif opc == "3":
            print (3)
        elif opc == "4":
            print (4)
        else: 
            print ("Ingrese un caracter del 1 al 4")
            time.sleep (2)
            print ("..")