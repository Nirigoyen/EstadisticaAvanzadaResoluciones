import math
import scipy.stats as st

import Auxiliares

def ComparacionDesvioEstandar():
    print("Cálculo del intervalo de confianza para la razón de varianzas")

    # Entrada de datos
    alfa = float(input("Ingrese el Riesgo (alfa): "))

    # Muestra 1
    n1 = int(input("Ingrese el tamaño muestral 1 (n1): "))
    s1 = float(input("Ingrese la varianza muestral 1 (s1): "))

    # Muestra 2
    n2 = int(input("Ingrese el tamaño muestral 2 (n2): "))
    s2 = float(input("Ingrese la varianza muestral 2 (s2): "))

    # Cálculos
    j2 = (s1 ** 2) / (s2 ** 2)
    nu1 = n1 - 1
    nu2 = n2 - 1

    a = j2 / st.f.ppf(1 - alfa / 2, nu1, nu2)
    b = j2 / st.f.ppf(alfa / 2, nu1, nu2)

    # Redondeo de límites
    a = math.floor(a * 10000) / 10000
    b = round(b, 4)

    if b - int(b) < 0.0001:
        b = int(b) + 1
    else:
        b = round(b + 0.0001, 4)

    # Resultado
    Auxiliares.mostrarResultadosLimites(a, b, alfa)



    # Preguntar si desea calcular n
    opcion = input("\n¿Desea calcular n? (s/n): ")

    if opcion.lower() == "s":

        # Calcular R
        r = b / a
        print(f"\nR calculado con B/A es: {r}")

        # Pedir R
        r = float(input("\nIngrese R (o presione Enter para calcular con B/A): "))
        if not r:
            r = b / a

        # Iteraciones para calcular n
        nu = 2
        tol = 1e-5
        dif = 1
        denominador = (math.sqrt(r) - 1) ** 2


        while dif > tol:
            nu_new = math.ceil((4 * st.t.ppf(1 - alfa / 2, nu) ** 2 * math.sqrt(r)) / denominador)
            dif = abs(nu_new - nu)
            nu = nu_new


        print(f"\nEl tamaño muestral n calculado es: {nu + 1}")

def ComparacionVarianzaMuestral():
    print("Cálculo del intervalo de confianza para la razón de varianzas")

    # Entrada de datos
    alfa = float(input("Ingrese el Riesgo (alfa): "))

    # Muestra 1
    n1 = int(input("Ingrese el tamaño muestral 1 (n1): "))
    s1 = float(input("Ingrese la varianza muestral 1 (s1): "))

    # Muestra 2
    n2 = int(input("Ingrese el tamaño muestral 2 (n2): "))
    s2 = float(input("Ingrese la varianza muestral 2 (s2): "))

    # Cálculos
    j2 = (s1 ** 2) / (s2 ** 2)
    nu1 = n1 - 1
    nu2 = n2 - 1

    a = j2 / st.f.ppf(1 - alfa / 2, nu1, nu2)
    b = j2 / st.f.ppf(alfa / 2, nu1, nu2)

    # Redondeo de límites
    a = math.floor(a * 10000) / 10000
    b = round(b, 4)

    if b - int(b) < 0.0001:
        b = int(b) + 1
    else:
        b = round(b + 0.0001, 4)

    # Resultado
    Auxiliares.mostrarResultadosLimites(a, b, alfa)

    # Preguntar si desea calcular n
    opcion = input("\n¿Desea calcular n? (s/n): ")

    if opcion.lower() == "s":

        # Calcular R
        r = b / a
        print(f"\nR calculado con B/A es: {r}")

        # Pedir R
        r = float(input("\nIngrese R (o presione Enter para calcular con B/A): "))
        if not r:
            r = b / a

        # Iteraciones para calcular n
        nu = 2
        tol = 1e-5
        dif = 1
        denominador = (math.sqrt(r) - 1) ** 2


        while dif > tol:
            nu_new = math.ceil((4 * st.t.ppf(1 - alfa / 2, nu) ** 2 * math.sqrt(r)) / denominador)
            dif = abs(nu_new - nu)
            nu = nu_new


        print(f"\nEl tamaño muestral n calculado es: {nu + 1}")