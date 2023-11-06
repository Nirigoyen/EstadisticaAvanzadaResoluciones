import math
import scipy as st

def HipotesisMediaConocidoDesvioInfinito():
    eleccion = None
    criterio = True
    print("Seleccione que criterio utilizara:")

    while eleccion != "1" or eleccion != "2":
        print("1. Criterio Pesimista (Ocasiones nuevas, Riesgos Economicos Muy Grandes, etc)")
        print("2. Criterio Optimista (Ocasiones rutinarias, Controles, etc)")
        eleccion = input("Seleccione que criterio utilizara: ")

        if eleccion == "-1":
            return
        elif eleccion == "1": #USO TRUE PARA CRITERIO OPTIMISTA, FALSE PARA CRITERIO PESIMISTA
            criterio = False

    alfa = float(input("Ingrese el riego a tomar(alfa): "))
    xRaya = float(input("Ingrese el valor de x̄: "))

    xComparativo = float(input("Ingrese el valor con el cual compara(X0): "))

    desvio = float(input("Ingrese el valor del desvio(): "))

    cantidad = int(input("Ingrese la tamaño de la muestra(n) (Ingrese -1 en caso de no tener n): "))

    if cantidad == -1:
        beta = float(input("Ingrese el valor de Beta: "))
        X1 = float(input("Ingrese el valor de µ1(Esta asociado a Beta): "))
        zBeta = st.norm.ppf(1-beta)
        zAlfa = st.norm.ppf(1-alfa)
        cantidad = (((zBeta + zAlfa) * desvio) / X1 - xComparativo) ** 2

    xCritico = xComparativo