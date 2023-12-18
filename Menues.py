import Estimaciones
import Hipotesis
import Comparaciones
import Contrastes


def MenuGeneral():
    posibilidades = ("-1", "1", "2", "3", "4")
    eleccion = None
    while eleccion != "-1":
        print("Bienvenido al resolvedor de Estadistica Avanzada")
        print("----" * 8)
        print("1. Estimaciones")
        print("2. Ensayos de Hipótesis")
        print("3. Comparacion de parametros")
        print("4. Contrastes Chi Cuadrado")
        print("----" * 8)
        eleccion = input("Ingrese que quiere calcular (Ingrese -1 para cerrar): ")

        if eleccion == "1":
            print("\n" * 100)
            MenuEstimaciones()
        elif eleccion == "2":
            print("\n" * 100)
            MenuHipotesis()
        elif eleccion == "3":
            print("\n" * 100)
            MenuComparacion()
        elif eleccion == "4":
            print("\n" * 100)
            MenuContrastes()
        elif eleccion == "-1":
            break
        else:
            print("El valor ingresado es incorrecto")
            print("\n" * 100)


def MenuEstimaciones():
    posibilidades = ("-1", "1", "2", "3")
    eleccion = None
    while eleccion != "-1":
        print("Bienvenido al Estimador de Parametros")
        print("----" * 8)
        print("1. Media(µ)")
        print("2. Varianza(σ²) o  Desvio Estandar(σ)")
        print("3. Proceso de Bernoulli(p)")
        print("----" * 8)
        eleccion = input("Ingrese que quiere calcular (Ingrese -1 para cerrar): ")

        if eleccion == "1":
            print("\n" * 100)
            MenuEstimacionesMedia()
        elif eleccion == "2":
            print("\n" * 100)
            MenuEstimacionesVarianza()
        elif eleccion == "3":
            print("\n" * 100)
            MenuEstimacionesBernoulli()
        elif eleccion == "-1":
            break
        else:
            print("El valor ingresado es incorrecto")
            print("\n" * 100)


def MenuHipotesis():
    posibilidades = ("-1", "1", "2", "3")
    eleccion = None
    while eleccion != "-1":
        print("Bienvenido al Portal de Ensayos de Hipotesis")
        print("----" * 8)
        print("1. Media(µ)")
        print("2. Varianza(σ²) o  Desvio Estandar(σ)")
        print("3. Proceso de Bernoulli(p)")
        print("----" * 8)
        eleccion = input("Ingrese que quiere calcular (Ingrese -1 para cerrar): ")

        if eleccion == "1":
            print("\n" * 100)
            MenuEstimacionesMedia()
        elif eleccion == "2":
            print("\n" * 100)
            MenuEstimacionesVarianza()
        elif eleccion == "3":
            print("\n" * 100)
            MenuEstimacionesBernoulli()
        elif eleccion == "-1":
            break
        else:
            print("El valor ingresado es incorrecto")
            print("\n" * 100)
def MenuComparacion():
    print("WIP")
def MenuContrastes():
    print("WIP")

#Menues de estimaciones
def MenuEstimacionesMedia():
    posibilidades = ("-1", "1", "2", "3", "4")
    eleccion = None
    while eleccion != "-1":
        print("Estimacion de Media(µ)")
        print("----" * 8)
        print("1. Desvio Conocido, Poblacion Infinita")
        print("2. Desvio Conocido, Poblacion Finita")
        print("3. Desvio Desconocido, Poblacion Infinita")
        print("4. Desvio Desconocido, Poblacion Finita")
        print("----" * 8)
        eleccion = input("Ingrese que quiere calcular (Ingrese -1 para volver): ")

        if eleccion == "1":
            print("\n" * 100)
            Estimaciones.EstimacionMediaConocidoDesvioInfinito()
        elif eleccion == "2":
            print("\n" * 100)
            Estimaciones.EstimacionMediaConocidoDesvioFinito()
        elif eleccion == "3":
            print("\n" * 100)
            Estimaciones.EstimacionMediaDesconocidoDesvioInfinito()
        elif eleccion == "4":
            print("\n" * 100)
            Estimaciones.EstimacionMediaDesconocidoDesvioFinito()
        elif eleccion == "-1":
            break
        else:
            print("El valor ingresado es incorrecto")
            print("\n" * 100)

def MenuEstimacionesVarianza():
    posibilidades = ("-1", "1", "2")
    eleccion = None
    while eleccion != "-1":
        print("Estimacion Varianza(σ²) o  Desvio Estandar(σ)")
        print("----" * 8)
        print("1. Varianza(σ²)")
        print("2. Desvio Estandar(σ)")
        print("----" * 8)
        eleccion = input("Ingrese que quiere calcular (Ingrese -1 para volver): ")

        if eleccion == "1":
            print("\n" * 100)
            Estimaciones.EstimacionVarianza()
        elif eleccion == "2":
            print("\n" * 100)
            Estimaciones.EstimacionDesvioEstandar()
        elif eleccion == "-1":
            break
        else:
            print("El valor ingresado es incorrecto")
            print("\n" * 100)

def MenuEstimacionesBernoulli():
    Estimaciones.EstimacionProcesoBernoulli()



