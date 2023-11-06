import math
import scipy.stats as st


#MENUES
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

#AUXILIARES
def mostrarResultadosLimites(a, b, alfa):
    print(f"Valor de A: {a:.4f}")
    print(f"Valor de B: {b:.4f}")
    print(f"\nResultado Final:\nP({a:.4f} ≤ p ≤ {b:.4f}) = {100 - 100 * alfa}%")

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

        error = z * (desvio / math.sqrt(n))

        # Resultado
        mostrarResultadosLimites(a, b, alfa)

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

        error = z * (desvio / math.sqrt(n)) * raiz

        mostrarResultadosLimites(a, b, alfa)

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

        error = t * (estimador_desvio / math.sqrt(n))

        mostrarResultadosLimites(a, b, alfa)

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

        error = t * (estimador_desvio / math.sqrt(n)) * raiz

        mostrarResultadosLimites(a, b, alfa)

        print(f"Error muestral actual: {error:.4f}")

        nuevo_error = input("Ingresa nuevo error muestral (dejar en blanco para terminar): ")
        if nuevo_error == "":
            break
        else:
            nuevo_error = float(nuevo_error)

            n_infinito = math.ceil((t * estimador_desvio / nuevo_error) ** 2)
            n_nuevo = int(N * n_infinito / (N + n_infinito))

            print(f"Nuevo tamaño muestral requerido: {n_nuevo}")

#Estimaciones de Desvio Estandar
def EstimacionDesvioEstandar():
    print("WIP")

def EstimacionVarianza():
    print("WIP")

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
    mostrarResultadosLimites(a, b, alfa)



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
    print(f"\nP({a:.4f} ≤ p ≤ {b:.4f}) = {100 - 100 * alfa}%")

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


if __name__ == '__main__':
    EstimacionProcesoBernoulli()
