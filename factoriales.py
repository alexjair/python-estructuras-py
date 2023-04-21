def factorial(n):
    """Calcula el factorial de n.

    Args:
        n int > 0: entero mayor que cero.
    """
    
    if n == 1:
        return 1
    
    return n * factorial( n - 1 )

#print('Factorial de n:' + str(factorial(4)))

n = int(input('Ingrece el Número a factorizar: '))

print('Factorial de n:' + str(factorial(n)))