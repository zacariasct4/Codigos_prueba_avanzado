empleados = ['Juan', 'María', 'Pedro', 'Alejandro']

empleados_ordenados = sorted(empleados)
empleados_ordenados2 = sorted(empleados, reverse=True)
print(empleados_ordenados)
print(empleados_ordenados2)

# Diccionarios

empleados_dict = [
    {'nombre': 'Juan', 'salario': 2000},
    {'nombre': 'María', 'salario': 3000},
    {'nombre': 'Pedro', 'salario': 2500},
    {'nombre': 'Alejandro', 'salario': 4000}
]

empleados_ordenados_salario = sorted(empleados_dict, key= lambda x: x['salario'])
print(empleados_ordenados_salario)
