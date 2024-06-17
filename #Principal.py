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
    except ValueError:    #Mensaje de error ,,,
        print ("Ingrese un caracter del 1 al 4")
    else:
        if opc == "1":
            funcion.registro();
            print()
            time.sleep (2)
        elif opc == "2":
            print (funcion.Lista_registro)
        elif opc == "3":
            try:
                imp = input ("1.- Imprimir todas las planillas \n2.- Imprimir una planilla \n3.- Salir \n-> ")
            except ValueError:
                print ("Elija una opcion del 1 al 3")
            else:
                if imp == "1":
                    print ()
                elif imp == "2":
                    print ()
                elif imp == "3":
                    print
                else:
                    print ("Elija una opcion valida")

        elif opc == "4":
            print ("Gracias por usar el programa, vuelva pronto.")
            break

        else: 
            print ("Ingrese un caracter del 1 al 4")
            time.sleep(2)
            print ("..")
