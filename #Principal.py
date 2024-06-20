import funciones as funcion
import time
import os
flag=True
logged_in = False
usuarios_registrados={'miguel':'123',
                      'arturo':'321',
                      'cait':'234'}
while flag:
    usuario=input("Ingrese su usuario: -> ");
    contraseña=input("Ingrese su contraseña: -> ");
    if  usuario in usuarios_registrados and contraseña == usuarios_registrados[usuario]:
        time.sleep(0.5)
        print(f"El inicio de sesion fue exitoso. !Bienvenid@ - @{usuario} ¡");
        time.sleep(0.5)
        logged_in = True
        while logged_in:
            print("\n:::: MENÚ DE OPCIONES ::::\n")
            print("1.- Registrar trabajador.")
            print("2.- Listar todos los trabajadores.")
            print("3.- Imprimir planilla de sueldos.")
            print("4.- Salir del programa.")
            try:
             opcion=int(input("Ingrese una opcion:-> "));    
            except ValueError:
                print("Ingrese una opcion valida del 1 al 4 ");
                continue;
            else:
                if opcion==1:
                    print(":::Registrar trabajador:::\n") 
                    funcion.resgistros();  
                elif opcion == 2 :
                    print(":::Listar todos los trabajadores:::\n")
                    funcion.monstrar_trabajadores();
                elif opcion == 3:
                    print(":::Imprimir planilla de sueldos:::\n")
                    funcion.crear_plantilla_txt
                elif opcion == 4:
                    print("...Saliendo del programa...")
                    time.sleep(1)
                    flag=False;
                    logged_in= False   
                else:
                    print("Ingrese una opción válida del 1 al 4")         
    else:
     print("\nCredenciales invalidas. Por favor, vuelva a intentarlo.\n")
