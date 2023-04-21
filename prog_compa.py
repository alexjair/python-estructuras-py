#Inicio
numero_usuarios_original = int(input('Favor de indicar el número de usuarios: '))
numero_usuarios = numero_usuarios_original
while numero_usuarios >= 1:
    if numero_usuarios == 0:
        break

#Bienvenida
    usuario = input('Bienvenido estimado usuario, favor de ingresar su nombre: ')

#Solicitando edad actual y calculando edad después del cumpleaños.
    edad_usuario = int(input('Favor de proporcionar su edad actual: '))
    edad_usuario += 1
    print('Gracias, ahora...')

#Fecha actual y próximo cumpleaños
    from datetime import datetime
    fecha_actual = datetime.now()

    dia_actual = datetime.strftime(fecha_actual, '%d')
    dia_actual = datetime.strptime(dia_actual, '%d')

    mes_actual = datetime.strftime(fecha_actual, '%b')
    mes_actual = datetime.strptime(mes_actual, '%b')

    print('Favor de proporcionar la fecha de su próximo cumpleaños conforme se le vaya solicitando')
    dia_proximo = (input('Día: '))
    mes_proximo = (input('Mes: '))
    año_proximo = (input('Año: '))
    print('')

    fecha_proximo = (f'{dia_proximo}/{mes_proximo}/{año_proximo}')
    fecha_proximo = datetime.strptime(fecha_proximo, '%d/%m/%Y')

#Cálculo de días restantes
    tiempo_restante = fecha_actual - fecha_proximo
    tiempo_restante = tiempo_restante.days
    tiempo_restante = tiempo_restante * -1

#Cambio de formato a la fecha del cumpleaños
    fecha_proximo = datetime.strftime(fecha_proximo, '%d %b %Y')

#Resultado
    print('Listo!')
    print(f'Dentro de {tiempo_restante} días, el {fecha_proximo} cumplirás {edad_usuario} años!')
    print('')

    numero_usuarios -= 1

    while numero_usuarios >= 1:
        print(f'Gracias por tu tiempo {usuario}, proseguimos con el siguiente usuario...')
        break

#Despedida del programa
if numero_usuarios_original == 1:
    print('Gracias por tu tiempo y atención, ten un lindo día...')
    print('Y felicidades anticipadas por tu próximo cumpleaños!!')
elif numero_usuarios_original == 2:
    print('Gracias a ambos por su atención, tengan un lindo día...')
    print('Y felicidades anticipadas a ambos!!')
else:
    print('Gracias a todos por su atención, espero tengan un lindo día...')
    print('Y felicidades anticipadas a los cumpleañeros!!')