import unittest   

"""
Notas 😃
Pruebas de caja de cristal

Se basan en el flujo del programa.
Prueba todos los caminos posibles de una función. Ramificaciones, bucles for y while, recursión.
Sirve para regression testing o mocks. Esto es, cuando ya se liberó el programa pero descubrimos un bug que queremos arreglar.
if: Debemos probar todas las condiciones.
for y recursión: Una donde no entre, otro donde entre una vez y otra donde entre varias.
while: Donde la condición de entrada sea falsa y otra donde probemos los break statements.
También debemos probar todas las excepciones.


"""

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

class PruebaDeCristalTest(unittest.TestCase):
    
    def test_es_mayor_de_edad(self):
        edad = 20
        resultado = es_mayor_de_edad(edad)
        
        self.assertEqual(resultado, True)
        
    def test_es_menor_de_edad(self):
        edad = 16
        resultado = es_mayor_de_edad(edad)
        
        self.assertEqual(resultado, False)

if __name__ == '__main__':
    #unittest.main()
    unittest.main(verbosity=2) # con "verbosity=2" el resultado del test se muestra mas detallado.
    