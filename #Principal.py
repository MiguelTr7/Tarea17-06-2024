import Funciones_Def as funcion
import time
#Creamos un menu de 4 opciones 
Cargos = ["CEO" , "Desarollador" , "Analista de datos"]

#Usuarios

user_1 = "Pablom"

user_2 = "SinNombre"

#Contraseñas

pass_1 = "1234"

pass_2 = "4321"

#Inicio Login
print ("**** LOGIN ****")
while True:
    user = input ("Ingrese nombre de usuario: ")
    passw = input ("Ingrese la contraseña: ")
    if user == user_1 and passw == pass_1 or user == user_2 and passw == pass_2:
        time.sleep (2)
        print ("..")
        time.sleep (2)
        print ("Bienvenido al sistema")
        time.sleep (2)
        print ("...")
        time.sleep (1)
        print ("1.- Registrar trabajador")
        print ("2.- Listar todos los trabajdores")
        print ("3.- Imprimir planillas del sueldo")
        print ("4.- Salir del programa")
        try:
            opc = input ("-> ")
        except ValueError:    #Mensaje de error ,,,
            print ("Ingrese un caracter del 1 al 4")
        else:
            if opc == "1":    #Registro ,,,,
                funcion.registro();
                print()
                time.sleep (2)
            elif opc == "2":   #Listar trabajadores ,,,
                print (funcion.Lista_registro)
            elif opc == "3":   #Imrpimir planillas ,,,
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

            elif opc == "4":   #Salir del programa ,,,
                print ("Gracias por usar el programa, vuelva pronto.")
                quit()

            else: 
                print ("Ingrese un caracter del 1 al 4")
                time.sleep(2)
                print ("..")
    else:
        time.sleep (2)
        print ("..")
        time.sleep (2)
        print ("Ingrese un nombre de usuario valido.")
        time.sleep (2)
        print ("..")
        time.sleep (2)
        print ("..")
        time.sleep (2)
        print ()
        print ()