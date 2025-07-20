#Simulador de votacion cruzada
print("---------BIENVENIDO AL REGISTRO DE VOTACIONES---------")
name = input("Ingrese nombre completo: ")
if len(name) < 5:
    print("Nombre invalido")
else:
    dep = input("Ingrese su departamento: ")
    if dep == "Peten" or dep == "Alta verapaz":
        año_nacimiento = int(input("Ingrese su año de nacimiento: "))
        if año_nacimiento > 2006 or dep != "Peten" or dep != "Alta verapaz":
            print("Debe ser mayor de edad para votar.")
        else:
            ID = (input("Ingrese su ID: "))
            if len(ID) != 13:
                print("DPI invalido, intente de nuevo.")
            else:
                print(f"Bienvenido{name}, su centro de votacion es {dep}")
