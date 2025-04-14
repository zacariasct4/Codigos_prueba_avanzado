
nombre_archivo = 'mi_archivo.txt'

# archivo = open(nombre_archivo, 'w')
# archivo.write('Hola\n')
# archivo.write('Como estas?')
# archivo.close()

# Bloque with. No hace falta cerrarlo ya que se cierra solo

with open(nombre_archivo, 'w') as archivo:
    archivo.write('Hola\n')
    archivo.write('Como estas?\n')

# Modo exclusivo. No sobreescribir un archivo

try:
    with open(nombre_archivo, 'x') as archivo:
        archivo.write('Hola\n')
        archivo.write('Estas bien?')
except Exception as e:
    print('El archivo ya existe')