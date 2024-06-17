import csv
Lista_registro = []
   
def registro():
    nombre = input("Ingrese su nombre: ");
    apellido = input("Ingrese su apellido: ");
    cargo = input("Ingrese su cargo: ");
    sueldo_bruto = float(input("Ingrese su sueldo bruto: "));
    Lista_registro.append({
        'Nombre': nombre,
        'Apellido': apellido,
        'Cargo': cargo,
        'Sueldo Bruto': sueldo_bruto
});
    print("Trabajador registrado exitosamente.")

def Boleta():
 with open('nuevo_archivo.csv', 'r', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        print(fila);
def lista_registro():
   


     
