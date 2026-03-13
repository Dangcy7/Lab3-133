import sys
input = sys.stdin.readline

# 1. PRE-CÁLCULO (Criba de Eratóstenes)
MAX = 10_000_000
es_primo = bytearray([1]) * (MAX + 1)
es_primo[0] = es_primo[1] = 0

for p in range(2, int(MAX ** 0.5) + 1):
    if es_primo[p]:
        cantidad = len(range(p * p, MAX + 1, p))
        es_primo[p * p: MAX + 1: p] = bytearray(cantidad)

# 2. PROCESAR ENTRADA
n = int(input())

for _ in range(n):
    a = int(input())  # Cada número en su propia línea
    b = int(input())

    inicio = min(a, b)
    fin = max(a, b)

    print(es_primo.count(1, inicio, fin + 1))