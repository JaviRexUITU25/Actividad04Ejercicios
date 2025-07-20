'''#Simulador de votacion cruzada
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

'''# Calculadora de impuestos progresivos + deducciones
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

#Sistema de autenticacion avanzado con penalizacion

users = []
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
        break
