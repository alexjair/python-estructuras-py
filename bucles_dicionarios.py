estudiantes = {
    'mexico': 10,
    'colombia': 15,
    'puerto_rico': 4,
}

print('for--normal');
for pais in estudiantes:
    print(pais)


print('for--keys');
for pais in estudiantes.keys():
    print(pais.key)

print('for--values()');
for numero_de_estudiantes in estudiantes.values():
    print(numero_de_estudiantes)

print('for--items()');
for pais, numero_de_estudiantes in estudiantes.items():
    print(str(numero_de_estudiantes) + ' ' + pais)
