import scipy.stats as ST
from math import exp2, ceil



def ComparacionDesvioEstandar():
    print("Valores de muestra 1:")
    print()
    S1 = float(input("Ingrese la varianza 1(S1): "))
    n1 = float(input("Ingrese la cantidad o tamaño 1(n1): "))

    print("Valores de muestra 2:")
    print()
    S2 = float(input("Ingrese la varianza 2(S2): "))
    n2 = float(input("Ingrese la cantidad o tamaño 2(n2): "))

    Alfa = float(input("Ingrese el valor de Alfa: "))

    j2 = exp2(S1) / exp2(S2)
    a = ceil(j2 / ST.f.ppf(q=1-Alfa, dfn=n1-1, dfd=n2-1))
    b = ceil(j2 / ST.f.ppf(q=Alfa, dfn=n1-1, dfd=n2-1))

    print("El valor de A es: ", a)
    print("El valor de B es: ", b)

    print("En el examen debe colocar:")
    print("P(", a, "≤ σ2 ≤ ", b, " = ", Alfa)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    ComparacionDesvioEstandar()
