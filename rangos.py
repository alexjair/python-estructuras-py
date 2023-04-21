

my_rango = range(0, 101, 1)

def funImpprimir(myrange):
    
    for i in myrange:
        if i % 2 != 0 and  i != 0:
            print('Impar: '+str(i))

funImpprimir(my_rango)