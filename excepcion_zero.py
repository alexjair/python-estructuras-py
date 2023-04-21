
import math 

#raiz cuadrada

def raiz_cuadrada_elementos_lista(lista, multiplicador):
    try:
        return [math.sqrt(i*multiplicador) for i in lista]
    except ValueError as e:
        print (e)
        return f'no existe la raíz cuadrada de un negativo'    

lista = list(range(10))
multiplicador = -8

print (raiz_cuadrada_elementos_lista(lista, multiplicador))

#ZERO

"""Creamos una función en donde cada elemento de 
una lista es dividida por un divisor definido"""

def divide_elementos_de_lista(lista, divisor):
    """El programa intentara realizar la división"""
    try:
        return [i / divisor for i in lista]
        """En caso de error de tipo ZeroDivisionError que
        significa error al dividir en cero, el programa
        ejecutara la siguiente instrucción"""
        
    except ZeroDivisionError as e:
        return lista

lista = list(range(10))
divisor = 0

print(divide_elementos_de_lista(lista, divisor))
