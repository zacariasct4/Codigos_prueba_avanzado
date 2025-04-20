import re

text = 'Python es lo mejor. Python es lo máximo. Python es fácil, pero ojo con Python que tiene su miga.'
pattern  = 'Python'
pattern2= 'mejor'
result = re.search(pattern, text)

if result:
    print(f'{pattern} está {len(re.findall(pattern, text))} veces en el texto')
else:
    print(pattern +' no se encuentra')

result2 = re.search(pattern2, text)
print(f'Se dice que Python es mejor a partir de {result2.start()} y termina en {result2.end()}')

# Uso de . y *
pattern3 = r'p.th*'
replacement = 'C++'
result3 = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
print(result3)

# Encontrar un caracter en concreto:  \
pattern4 = r'\,'

result4 = re.search(pattern4, text)

print(f'La coma se encuentra en el puesto {result4.end()}')

# \d{'número de dígitos'} búsqueda de dígitos
# \s para saltos de línea
# \w caracteres alfanuméricos
# \^ para indicar con qué tiene que empezar: \^w{4,6} (debe empezar con caracter alfanumérico de 4 a 6 caracteres)
# \$ para indicar con qué debe terminar: \.$ (debe acabar con punto)
# \b coincide con el principio o final de una palabra: \bc.sa\b
# | coincidir con una u otra opción: r'palta|aguacate|\b\w{7}\b|p..a'
# + una vez o más veces: \a+  ('aaa aa bb a cc') serían 3 veces
