import csv
Lista_registro = []
des_salud=0.07
des_afp=0.12
def registro():
    nombre=input("Ingrese su nombre: ");
    apellido=input("Ingrese su apellido: ");
    cargo= input("Ingrese su cargo: ");
    sueldo_bruto =int(input("Ingrese su sueldo bruto: "));
    Lista_registro.append({
        'Nombre': nombre,
        'Apellido': apellido,
        'Cargo': cargo,
        'Sueldo Bruto': sueldo_bruto,
        'Descuento Salud': desc_salud,
        'Descuento AFP': desc_afp,
        'Sueldo Líquido': sueldo_liquido
    })
    desc_salud=(sueldo_bruto*des_salud );
    desc_afp=(sueldo_bruto*des_afp);
    sueldo_liquido=(sueldo_bruto-desc_salud-desc_afp);
    print("Trabajador registrado exitosamente.")

def Boleta():
 with open('nuevo_archivo.csv', 'r', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        print(fila);
def lista_registro():
   
   


     
