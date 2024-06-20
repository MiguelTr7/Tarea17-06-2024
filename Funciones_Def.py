cargo_disponibles = ["Ceo","Desarrollador","Administrador"]
lista_registros=[]
#Definir los registros
def resgistros():
    nombre=input("ingrese su nombre: -> ").title()
    apellido=input("Ingrese su apellido: -> ").title()
    cargo=input(f"Cargos disponibles {cargo_disponibles} \nIngrese su cargo: -> ").title();
    while cargo not in cargo_disponibles :
        print("Cargo no valido.Los cargos disponibles son:", cargo_disponibles);
        cargo=input("Ingrese el cargo del trabajador nuevamente: -> ").title();
    try:  
     sueldo=int(input("Ingrese su sueldo bruto: -> "));
    except ValueError:
     print("Ingrese caracteres validos.");
    trabajador={'Nombre':nombre,
                'Apellido':apellido,
                'Cargo':cargo,
                'Sueldo':sueldo};
    lista_registros.append(trabajador);
    print(":Trabajador registrado exitosamente:");
    crear_plantilla_txt(nombre,apellido,cargo,sueldo);
#Para calcular los descuentos
def calcular_sueldo_liquido (sueldo_bruto):
    descuento_salud=int(sueldo_bruto*0.07)
    descuento_afp=int(sueldo_bruto*0.12)
    sueldo_liquido=int(sueldo_bruto-(descuento_salud+descuento_afp));
    return descuento_salud,descuento_afp,sueldo_liquido
#Para crear los archivos .txt
def crear_plantilla_txt(nombre,apellido,cargo,sueldo):
    descuento_salud,descuento_afp,sueldo_liquido = calcular_sueldo_liquido (sueldo)
    with open("registros_usuarios.txt","a") as archivo:
     archivo.write(f"Nombre: {nombre} {apellido}\n");
     archivo.write(f"Cargo: {cargo} \n")
     archivo.write(f"Sueldo Bruto: {sueldo}\n")
     archivo.write(f"Descuento Salud:{descuento_salud} \n")
     archivo.write(f"Descuento AFP:{descuento_afp} \n")
     archivo.write(f"Sueldo liquido total:{sueldo_liquido} \n")
     archivo.write(f"")
def monstrar_trabajadores():
   if len(lista_registros) == 0:
      print("No hay trabajadores en el sistema")
   else:
      print("Lista de trabajadores registrados")
      for i, trabajador in enumerate(lista_registros,start=1):
         nombre = trabajador['Nombre']
         apellido = trabajador['Apellido']
         cargo = trabajador['Cargo']
         print(f"{i}-. {nombre} {apellido}- {cargo}")
         
