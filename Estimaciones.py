import math
import scipy.stats as st

import Auxiliares

#ESTIMACIONES

#Estimaciones de Medias(Mu)
def EstimacionMediaConocidoDesvioInfinito():
    while True:

        desvio = float(input("Ingresa el desvio estándar de la población (σ): "))

        alfa = float(input("Ingresa el nivel de significancia (α): "))

        prom_datos = float(input("Ingresa el promedio obtenido (X̅): "))

        n = int(input("Ingresa la cantidad de observaciones (n): "))

        z = st.norm.ppf(1 - alfa / 2)

        a = prom_datos - z * (desvio / math.sqrt(n))
        b = prom_datos + z * (desvio / math.sqrt(n))

        # Redondeo de límites
        a = math.floor(a * 10000) / 10000
        b = round(b, 4)

        if b - int(b) < 0.0001:
            b = int(b) + 1
        else:
            b = round(b, 4)

        error = z * (desvio / math.sqrt(n))

        # Resultado
        Auxiliares.mostrarResultadosLimites(a, b, alfa)

        print(f"Error muestral actual: {error:.4f}")

        nuevo_error = input("Ingresa nuevo error muestral (dejar en blanco para terminar): ")
        if nuevo_error == "":
            break
        else:
            nuevo_error = float(nuevo_error)
            n_nuevo = math.ceil((z * desvio / nuevo_error) ** 2)
            print(f"Nuevo tamaño muestral requerido: {n_nuevo}")

    print("Programa finalizado")

def EstimacionMediaConocidoDesvioFinito():
    while True:

        n = int(input("Ingresa la cantidad de observaciones (n): "))

        N = int(input("Ingresa el tamaño de la población (N): "))

        desvio = float(input("Ingresa el desvío estándar de la población (σ): "))

        alfa = float(input("Ingresa el nivel de significancia (α): "))

        prom_datos = float(input("Ingresa el promedio obtenido (X̅): "))

        z = st.norm.ppf(1 - alfa / 2)

        raiz = math.sqrt((N - n) / N)

        a = prom_datos - z * (desvio / math.sqrt(n)) * raiz
        b = prom_datos + z * (desvio / math.sqrt(n)) * raiz

        # Redondeo de límites
        a = math.floor(a * 10000) / 10000
        b = round(b, 4)

        if b - int(b) < 0.0001:
            b = int(b) + 1
        else:
            b = round(b, 4)

        error = z * (desvio / math.sqrt(n)) * raiz

        Auxiliares.mostrarResultadosLimites(a, b, alfa)

        print(f"Error muestral actual: {error:.4f}")

        nuevo_error = input("Ingresa nuevo error muestral (dejar en blanco para terminar): ")
        if nuevo_error == "":
            break
        else:
            nuevo_error = float(nuevo_error)

            n_infinito = math.ceil((z * desvio / nuevo_error) ** 2)
            n_nuevo = int(N * n_infinito / (N + n_infinito))

            print(f"Nuevo tamaño muestral requerido: {n_nuevo}")

    print("Programa finalizado")

def EstimacionMediaDesconocidoDesvioInfinito():
    while True:

        n = int(input("Ingresa la cantidad de observaciones (n): "))

        estimador_desvio = float(input("Ingresa el estimador de desviación (S): "))

        alfa = float(input("Ingresa el nivel de significancia (α): "))

        prom_datos = float(input("Ingresa el promedio obtenido (X̅): "))

        t = st.t.ppf(1 - alfa / 2, n - 1)

        a = prom_datos - t * (estimador_desvio / math.sqrt(n))
        b = prom_datos + t * (estimador_desvio / math.sqrt(n))

        # Redondeo de límites
        a = math.floor(a * 10000) / 10000
        b = round(b, 4)

        if b - int(b) < 0.0001:
            b = int(b) + 1
        else:
            b = round(b, 4)

        error = t * (estimador_desvio / math.sqrt(n))

        Auxiliares.mostrarResultadosLimites(a, b, alfa)

        print(f"Error muestral actual: {error:.4f}")

        nuevo_error = input("Ingresa nuevo error muestral (dejar en blanco para terminar): ")
        if nuevo_error == "":
            break
        else:
            nuevo_error = float(nuevo_error)
            n_nuevo = math.ceil((t * estimador_desvio / nuevo_error) ** 2)
            print(f"Nuevo tamaño muestral requerido: {n_nuevo}")

def EstimacionMediaDesconocidoDesvioFinito():
    while True:

        n = int(input("Ingresa la cantidad de observaciones (n): "))

        N = int(input("Ingresa el tamaño de la población (N): "))

        estimador_desvio = float(input("Ingresa el estimador de desviación (S): "))

        alfa = float(input("Ingresa el nivel de significancia (α): "))

        prom_datos = float(input("Ingresa el promedio obtenido (X̅): "))

        t = st.t.ppf(1 - alfa / 2, n - 1)

        raiz = math.sqrt((N - n) / N)

        a = prom_datos - t * (estimador_desvio / math.sqrt(n)) * raiz
        b = prom_datos + t * (estimador_desvio / math.sqrt(n)) * raiz

        # Redondeo de límites
        a = math.floor(a * 10000) / 10000
        b = round(b, 4)

        if b - int(b) < 0.0001:
            b = int(b) + 1
        else:
            b = round(b, 4)

        error = t * (estimador_desvio / math.sqrt(n)) * raiz

        Auxiliares.mostrarResultadosLimites(a, b, alfa)

        print(f"Error muestral actual: {error:.4f}")

        nuevo_error = input("Ingresa nuevo error muestral (dejar en blanco para terminar): ")
        if nuevo_error == "":
            break
        else:
            nuevo_error = float(nuevo_error)

            n_infinito = math.ceil((t * estimador_desvio / nuevo_error) ** 2)
            n_nuevo = int(N * n_infinito / (N + n_infinito))

            print(f"Nuevo tamaño muestral requerido: {n_nuevo}")

#Estimaciones de Desvio Estandar y Varianza
def EstimacionDesvioEstandar():
    print("WIP")
#VERIFICAR
def EstimacionVarianza():
    while True:

        s2 = float(input("Ingresa la varianza muestral (S2): "))

        n = int(input("Ingresa el tamaño muestral (n): "))

        alfa = float(input("Ingresa el nivel de significancia (α): "))

        chi_inf = st.chi2.ppf(alfa / 2, n - 1)
        chi_sup = st.chi2.ppf(1 - alfa / 2, n - 1)

        A = (n - 1) * s2 / chi_sup
        B = (n - 1) * s2 / chi_inf

        error = (B - A) / 2
        relacion = B / A

        Auxiliares.mostrarResultadosLimites(A, B, alfa)
        print(f"Error muestral: {error:.4f}")
        print(f"Relación B/A: {relacion:.4f}")

        nueva_relacion = input("Ingresa nueva relación deseada (dejar en blanco para terminar): ")

        if nueva_relacion == "":
            break
        else:
            nueva_relacion = float(nueva_relacion)

            a = (st.norm.ppf(1 - alfa / 2) * (nueva_relacion ** (1 / 3) + 1)) / (2 * (nueva_relacion ** (1 / 3) - 1))
            v = 2 / 9 * (a + math.sqrt(a ** 2 + 1)) ** 2
            n_nuevo = int(math.ceil(v + 1))

            print(f"Nuevo tamaño muestral requerido: {n_nuevo}")


#Estimaciones Proceso de Bernoulli
def EstimacionProcesoBernoulli():
    # Inputs
    n = int(input("Ingrese la cantidad de observaciones (n): "))
    r = int(input("Ingrese la cantidad de éxitos obtenidos (r): "))
    alfa = float(input("Ingrese el nivel de significancia (alfa): "))

    # Cálculo
    p = r / n
    print("p̂ = ", p)
    a = 1 / (1 + ((n - r + 1) / r) * st.f.ppf(1 - alfa / 2, 2 * n - 2 * r + 2, 2 * r))
    denominador = ((r + 1) * st.f.ppf(1 - alfa / 2, 2 * r + 2, 2 * n - 2 * r))

    b = 1 / (1 + (n - r) / denominador)

    # Redondeo de límites
    a = math.floor(a * 10000) / 10000
    b = round(b, 4)

    if b - int(b) < 0.0001:
        b = int(b) + 1
    else:
        b = round(b, 4)

    # Resultado
    print(f"Valor de A: {a:.4f}")
    print(f"Valor de B: {a:.4f}")
    print(f"\nResultado Final:\nP({a:.4f} ≤ p ≤ {b:.4f}) = {100 - 100 * alfa}%")

    # Queda calculo de N por Aproximacion Poisson/Normal