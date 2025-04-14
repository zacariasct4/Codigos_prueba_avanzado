
def generador(maximo):

    contador = 0
    while contador < maximo:
        yield contador  # pone en pausa la función 
        contador += 1

var_generador = generador(5)

for valor in var_generador:
    print(valor)


# Expresiones generadoras

lista_generador = (x**2 for x in range(10) if x % 2 == 0)

for cuadrado_pares in lista_generador:
    print(cuadrado_pares)

