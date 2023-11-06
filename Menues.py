def MenuGeneral():
    posibilidades = ("-1", "1", "2", "3", "4")
    eleccion = None
    while eleccion not in posibilidades:
        print("Bienvenido al resolvedor de Estadistica Avanzada")
        print("----" * 8)
        print("1. Estimaciones")
        print("2. Ensayos de Hipótesis")
        print("3. Comparacion de parametros")
        print("4. Contrastes Chi Cuadrado")
        print("----" * 8)
        eleccion = input("Ingrese que quiere calcular (Ingrese -1 para cerrar): ")

        if eleccion == "1":
            MenuEstimaciones()
        elif eleccion == "2":
            MenuHipotesis()
        elif eleccion == "3":
            MenuComparacion()
        elif eleccion == "4":
            MenuContrastes()
        elif eleccion == "-1":
            break
        else:
            print("El valor ingresado es incorrecto")

        print("\n" * 100)


def MenuEstimaciones():
    print("WIP")
def MenuHipotesis():
    print("WIP")
def MenuComparacion():
    print("WIP")
def MenuContrastes():
    print("WIP")