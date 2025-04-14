
nombre_archivo = 'mi_archivo.txt'

with open(nombre_archivo, 'r') as archivo:
    # print(archivo.readlines())
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea.strip())  # Elimina todos los caracteres al inicio y al final

# Leer usando read

with open(nombre_archivo, 'r') as archivo:
    print(archivo.read())