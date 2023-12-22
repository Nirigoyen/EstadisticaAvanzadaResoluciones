#AUXILIARES
def mostrarResultadosLimites(a, b, alfa):
    print(f"Valor de A: {a:.4f}")
    print(f"Valor de B: {b:.4f}")
    print(f"\nResultado Final:\nP({a:.4f} ≤ p ≤ {b:.4f}) = {100 - 100 * alfa}%")
    print("En caso de haber colocado unicamente uno de los limites, tener en cuenta unicamente dicho limite.")