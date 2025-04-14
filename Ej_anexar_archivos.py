
nombre_archivo = 'mi_archivo.txt'

with open(nombre_archivo, 'a') as archivo:
    archivo.write('Estoy incluyendo información\n')

with open(nombre_archivo, 'r') as archivo:
    print(archivo.read())