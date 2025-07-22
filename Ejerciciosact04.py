'''#Simulador de votacion cruzada 1
print("---------BIENVENIDO AL REGISTRO DE VOTACIONES---------")
name = input("Ingrese nombre completo: ")
if len(name) < 5:
    print("Nombre invalido")
else:
    dep = input("Ingrese su departamento: ")
    año_nacimiento = int(input("Ingrese su año de nacimiento: "))
    if año_nacimiento > 2006 and dep != "Peten" and dep != "Alta verapaz":
        print("Debe ser mayor de edad para votar.")
    else:
        ID = (input("Ingrese su ID: "))
        if len(ID) != 13:
            print("DPI invalido, intente de nuevo.")
        else:
            print(f"Bienvenido {name}, su centro de votacion es {dep}")
    if año_nacimiento > 2007:
        print("Debe ser mayor de edad para votar.")'''
from tkinter.filedialog import dialogstates

'''# Calculadora de impuestos progresivos + deducciones 2
ingreso_anual = int(input("Ingrese su ingreso anual: "))
dependiente = int(input("Ingrese el numero de dependientes: "))
if 0 < ingreso_anual <= 30000:
    print(f"La cantidad de impuestos a pagar es: {(ingreso_anual * 5) / 100} Quetzales")
if 30001 < ingreso_anual <= 60000:
    print(f"La cantidad de impuestos a pagar es: {(ingreso_anual * 10) / 100} Quetzales")
if 60001 < ingreso_anual <= 100000:
    print(f"La cantidad de impuestos a pagar es: {(ingreso_anual * 15) / 100} Quetzales")
if ingreso_anual > 100000:
    print(f"La cantidad de impuestos a pagar es: {(ingreso_anual * 20) / 100} Quetzales")
if ingreso_anual < 40000 and dependiente < 2:
    print("No se paga impuestos")'''

#Sistema de autenticacion avanzado con penalizacion 3

'''users = []
passwords = "12345"
psuser = ""
numero_intentos = 3
while numero_intentos > 0:
    print("------BIENVENIDO USUARIO------")
    psuser = input("Ingrese su contraseña: ")
    if psuser != passwords:
        print("Contraseña incorrecta,intente de nuevo.")
        numero_intentos -=1
    else:
        print("¡Bienvenido usuario!")
        print("BIENVENIDO USUARIO")
        print("1. Ver perfil.\n"
              "2. Cambiar contraseña.\n"
              "3. Cerrar sesion.\n"
              "------ELIJA UNA OPCION------")
        break
    if numero_intentos == 0:
        print("----------------------------ACCESO BLOQUEADO----------------------------")
        break'''

'''#Simulador de facturacion con IVA, descuentos y propina 4
milk = 30
eggs = 40
shopping = []
while True:
    print("-----MENU DE PRODUCTOS------\n"
                    "1. Leche\n"
                    "2. Huevos\n"
                    "5. Salir\n")
    request = int(input("Seleccione el producto que desea cotizar: "))
    if request == 1:
        print(f"La Leche tiene un valor de Q{milk}.\n"
                      "1. Si\n"
                      "2. No\n")
        price1= int(input("¿Desea añadirla?: "))
        if price1 == 1:
            print("La leche ha sido agregada al carrito\n"
                  "1.Si\n"
                  "2.No\n")
        total = int(input("1.Si\n"
                          "2.No\n"
                          "¿Desea dejar propina?: "))
        if total == 1:
            tip = int(input("Cuanto % de propina quiere agregar?: "))
            frequent = int(input("1. Si\n"
                                 "2. No\n"
                                 "¿Tiene tarjeta de cliente frecuente?: "))
            if frequent == 1:
                    print (f"Su total con descuento es: Q.{(milk * 10)/100} \n")
            elif frequent == 2:
                print(f"Su total es de: Q.{milk}\n ")
        elif total == 2:
            frequent = int(input("1. Si\n"
                                 "2. No\n"
                                 "¿Tiene tarjeta de cliente frecuente?: "))
            if frequent == 1:
                    print (f"Su total con descuento es: Q.{(milk * 10)/100}\n")
            if frequent == 2:
                print(f"Su total es de: Q.{milk}\n ")
    elif request == 2:
        print(f"Los huevos tienen un valor de Q{eggs}.\n"
              "1. Si\n"
            "2. No\n")
        price1= int(input("¿Desea añadirla?: "))
        if price1 == 1:
            print("Los huevos han sido agregados al carrito\n"
                  "1.Si\n"
                  "2.No\n")
        final_price = int(input("¿Desea seguir comprando?: "))
        if final_price == 1:
             print("")
        shopping.append((price1, final_price))
        if price1 == 2:
            print("1. Si\n"
                "2.No\n")
        total = int(input("1.Si\n"
                          "2.No\n"
                          "¿Desea dejar propina?: "))
        if total == 1:
            tip = int(input("Cuanto % de propina quiere agregar?: "))
            frequent = int(input("1. Si\n"
                                 "2. No\n"
                                 "¿Tiene tarjeta de cliente frecuente?: "))
            if frequent == 1:
                    print (f"Su total con descuento es: Q.{(eggs * 10)/100} \n")
            elif frequent == 2:
                print(f"Su total es de: {eggs}\n ")
                iva_add = final_price + (final_price * 12) / 100
        elif total == 2:
            frequent = int(input("1. Si\n"
                                 "2. No\n"
                                 "¿Tiene tarjeta de cliente frecuente?: "))
            if frequent == 1:
                    print (f"Su total con descuento es: Q.{(eggs * 10)/100}\n")
            if frequent == 2:
                print(f"Su total es de: Q.{eggs}\n ")
                iva_add = final_price + (eggs * 12) / 100
    else:
            factura =int(input(""))'''


#Verificador de fecha válida 5
day = int(input("Ingrese el dia: "))
month = int(input("Ingrese el mes: "))
year = int(input("Ingrese el año: "))
leap = (year % 4 == 0 and year % 100 != 0 and year % 400 == 0)
days = [31,28,31,30,31,30,31,31,30,31,30,31]
if leap:
    days[1]=29
if 1 <day > days[month -1]:
    print("Dia invalido")
elif 1 < month > 12:
    print("Mes invalido")
else:
    q = day
    m = month
    y = year
    if m < 3:
        m += 12
        y -=1
    k = y % 100
    j = y // 100
    h = (q + (13 * (m + 1)) //5 + k + (k// 4) + (j//4) + 5 * j) % 7
    week =


'''#Clasificador de envio con multiples condiciones 6
print("---------------------Clasificador de envios---------------------")
package_weight = int(input("Ingrese el peso del paquete(kg): "))
distance = int(input("Ingrese la distancia del paquete(km): "))
urgent = int(input("1. Si\n"
                   "2. No\n"
                   "¿El pedido es urgente?: "))
size = int(input("Ingrese el tamaño del paquete:"
             "1. Grande\n"
             "2. Mediano\n"
             "3. Pequeño\n "))
if urgent == 1:
    total_price = 40
    print(f"Envio total: Q{total_price + 50}.")
if size == 1:
    total_price = 40
    print(f"Envio total: Q{total_price + 30}.")
if urgent == 2 and package_weight <5:
    total_price = 40
    print(f"Envio total: Q{total_price - 20}.")
else:
    total_price = 40
    print(f"Envio total: Q{total_price}.")'''

# Sistema de calificaciones con curva 7
'''names = {}
dictionarie = {}
for i in range(5):
    r_names = input("Ingrese nombre: ")
    r_notes1 = int(input("Ingrese Nota:"))
    r_notes2 = int(input("Ingrese Nota:"))
    r_notes3 = int(input("Ingrese Nota:"))
    names[r_names] = [r_notes1, r_notes2, r_notes3]
    dictionarie[r_names] = (r_notes1 + r_notes2 + r_notes3) / 3
    print(f"Promedio: {[[dictionarie[r_names]]]}")
for i in dictionarie:
    print("Promedio final: ")
    if dictionarie[i] > 70: break
else:
    for y in names:
        names[y] = [names[y][0] + 5, names[y][1] + 5, names[y][2] + 5]
        dictionarie[y] = sum(names[y])/3
print(f"------TABLA-----\n"
      f"{dictionarie}")'''

#CALCULADORA de rumbo entre puntos cardinales 8
while True:
    direction = int(input("------RUMBO------\n"
          "-"*5 + "Elija la opcion:"
                  "1. Norte a sur"
                  "2. Norte a este"
                  "3. Norte a oeste"
                  "4. Sur a norte"
                  "5. Sur a este"
                  "6. Sur a oeste"
                  "7. Este a norte"
                  "8. Este a sur"
                  "8. Este a oeste"
                  "9. Oeste a norte"
                  "10. Oeste a sur"
                  "10. Oeste a este"))
    if direction == 1:
        print("Debes ir recto")
    if direction == 2:
        print("")


