import csv
Lista_registro = [];
des_salud=0.07;
des_afp=0.12;
def registro():
    nombre=input("Ingrese su nombre: ");
    apellido=input("Ingrese su apellido: ");
    cargo= input("Ingrese su cargo: ");
    sueldo_bruto =int(input("Ingrese su sueldo bruto: "));
    desc_salud=sueldo_bruto*des_salud;
    desc_afp=sueldo_bruto*des_afp;
    sueldo_liquido=sueldo_bruto-desc_salud-desc_afp;
    print("Trabajador registrado exitosamente.");
    Lista_registro.append({
        'Nombre': nombre,
        'Apellido': apellido,
        'Cargo': cargo,
        'Sueldo Bruto': sueldo_bruto,
        'Descuento Salud': desc_salud,
        'Descuento AFP': desc_afp,
        'Sueldo Líquido': sueldo_liquido
    });
print("Trabajador registrado exitosamente.")
"""""Esto Salie en error
def imprimir_planilla(trabajadores_filtrados,):
    with open('planilla_trabajadores', "w",encoding='utf-8') as archivo:
        for trabajador in trabajadores_filtrados:
            archivo.write(f"Nombre: {trabajador['Nombre']}\n")
            archivo.write(f"Cargo: {trabajador['Cargo']}\n")
            archivo.write(f"Sueldo Bruto: {trabajador['Sueldo Bruto']}\n")
            archivo.write(f"Desc. Salud: {trabajador['Descuento Salud']}\n")
            archivo.write(f"Desc. AFP: {trabajador['Descuento AFP']}\n")
            archivo.write(f"Líquido a pagar: {trabajador['Sueldo Líquido']}\n")
            archivo.write("==============================\n")
"""

     
