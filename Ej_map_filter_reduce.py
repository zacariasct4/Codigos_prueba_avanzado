import functools


numeros = range(1,10+1)


# Uso de map
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)

# Uso de filter
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

# Uso de reduce

# reduce 

suma_acumulativa = functools.reduce(lambda x, y: x + y, numeros)
print(suma_acumulativa)