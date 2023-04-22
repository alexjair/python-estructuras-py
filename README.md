# 🛒 Python-Estructuras-Python:

Ejemplos y uso de **Estructuras en Python**, bucles, pruebas de **caja negra** e cristal, tuplas, recursividad, **exepciones** y **debugging**. Para poder ver los ejemplos, correr los codigos en consola..

- Autor: **Alexander Jair Rojas Paria**
- Email: alexjair@gmail.com

# Docstring

Leer la documentación de funciones:

\>\>help(nombre_funcion) (enter)

## **Pruebas de Caja Negra**

Las pruebas de caja negra se basan en la especificación de la función o el programa, aquí debemos probar sus **inputs** y validar los **outputs**. Se llama caja negra por que no necesitamos saber necesariamente los procesos internos del programa, solo contrastar sus resultados.

Estos tipos de pruebas son muy importantes para 2 tipos de test:

-   **Unit testing**: se realizan pruebas a cada uno de los módulos para determinar su correcto funcionamiento.
-   **Integration testing**: es cuando vemos que todos los módulos funcionan entre sí.

Es una buena práctica realizar los test antes de crear tus lineas de código, esto es por que cualquier cambio que se realice a futuro los *test* estaran incorporados para determinar si los cambios cumplen lo esperado.

En Python existe la posibilidad de realizar *test* gracias a la libreria unittest. Puede ser que el siguiente código no lo entiendas en su totalidad, pero en una próxima guía detallare mas el tema de *clases* en programación. Por ahora te mostrare como se realizan estos *test*.

```javascript

"""Importamos la libreria de unittest."""

**import** unittest

"""Creamos una clase para los test, en este caso se llamara

CajaNegraTest, y como parámetro."""

**class** **CajaNegraTest**(unittest.TestCase):

"""Definimos la funcion que generara el test."""

**def** **test_suma_dos_positivos**(self):

"Para nuestro ejemplo usaremos 2 parametros."""

num_1 = 10

num_2 = 5

"""Y dentro de la variable resultado

guardaremos lo que nos retornara la función suma."""

resultado = suma(num_1, num_2)

"""Y para terminar definimos la variable resultado

y cual es el valor esperado."""

self.assertEqual(resultado, 15)

"""Para definir el módulo de Python escribimos lo siguiente."""

**if** \__name_\_ == '__main__':

unittest.main()
```

Luego de escribir nuestro archivo iremos a la consola y ejecutaremos el *test*

python3 caja_negra.py

E \# Obtenemos un error en nuestro test

======================================================================

ERROR: test_suma_dos_positivos (__main__.CajaNegraTest) \# Veremos aqui el test con error

\----------------------------------------------------------------------

Traceback (most recent call last):

File "caja_negra.py", line 9, **in** test_suma_dos_positivos

resultado = suma(num_1, num_2)

NameError: name 'suma' is not defined \# La función suma no esta definida

\----------------------------------------------------------------------

Ran 1 test **in** 0.000s

FAILED (errors=1)

Como vimos en el recuadro anterior no definimos la función suma, para ello vamos a crearla.

**import** unittest

**def** **suma**(num_1, num_2):

**return** num_1 + num_2

**class** **CajaNegraTest**(unittest.TestCase):

**def** **test_suma_dos_positivos**(self):

num_1 = 10

num_2 = 5

resultado = suma(num_1, num_2)

self.assertEqual(resultado, 15)

**if** \__name_\_ == '__main__':

unittest.main()

Ahora ejecutaremos denuevo nuestro *test* en la terminal.

python3 caja_negra.py

.

\----------------------------------------------------------------------

Ran 1 test **in** 0.000s

OK

## **\*\* 7 principios de Testing \*\* de acuerdo al libro de ISTQB.**

**1 Las pruebas muestran la presencia de defectos  
**Significa que las pruebas pueden demostrar que EXISTEN problemas, pero no que los problemas NO EXISTEN.  
El objetivo principal de llevar a cabo una prueba es para detectar defectos. Trabajando bajo la premisa de que cada producto contiene defectos de algún tipo, una prueba que revela los errores es generalmente mejor que una que no lo hace. Todas las pruebas por lo tanto, deben ser diseñados para revelar tantos errores como sea posible

**2 Las pruebas exhaustivas son imposibles***  
*Las pruebas exhaustivas tratan de cubrir todas las combinaciones posibles de datos en el software, a fin de garantizar que ninguna situación puede surgir, una vez probado el software se ha liberado. Excepto en aplicaciones muy simples, el número de combinaciones posibles de datos es demasiado alta, es más eficaz y eficiente que los ingenieros de pruebas se centren en las funcionalidades de acuerdo a riesgos y prioridades.

**3 Pruebas tempranas.  
**Un producto (incluyendo los documentos, tales como la especificación del producto) se puede probar tan pronto como se ha creado. ISTQB recomienda probar un producto tan pronto como sea posible, corregir los errores más rápidamente posible. Los estudios han demostrado que los errores identificados al final del proceso de desarrollo por lo general cuestan más para resolver.  
Por ejemplo: un error encontrado en las especificaciones puede ser bastante sencillo de solucionar. Sin embargo, si ese error se transfiere a la codificación de software, una vez descubierto el error puede ser muy costoso y consume tiempo.

**4 Agrupamiento de Defectos  
**Los estudios sugieren que los problemas en un elemento de software tienden a agruparse en torno a un conjunto limitado de módulos o áreas. Una vez que estas áreas han sido identificadas, los administradores eficientes de prueba son capaces de enfocar las pruebas en las zonas sensibles, mientras que siguen buscando los errores en los módulos de software restantes. Me recuerda al 80/20.

**5 La paradoja del “Pesticida”  
**Al igual que el sobre uso de un pesticida, un conjunto de pruebas que se utilizan repetidamente en él disminuirá en su eficacia. Usando una variedad de pruebas y técnicas expondrá una serie de defectos a través de las diferentes áreas del producto.

**6 La prueba es dependiente del contexto  
**Las mismas pruebas no se deben aplicar en todos los ámbitos. Distintos productos de software tienen diferentes requisitos, funciones y propósitos. Una prueba diseñada para realizarse en un sitio web, por ejemplo, puede ser menos eficaz cuando se aplica a una aplicación de intranet. Una prueba diseñada para una forma de pago con tarjeta de crédito puede ser innecesariamente rigurosa si se realiza en un foro de discusión.  
En general, cuanto mayor es la probabilidad y el impacto de los daños causados ​​por el software fallado, mayor es la inversión en la realización de pruebas de software.

**7 La falacia de ausencia de errores  
**Declarar que una prueba no ha descubierto ningún error no es lo mismo que declarar que el software es “libre de errores”. Con el fin de garantizar que los procedimientos adecuados de software de prueba se lleva a cabo en todas las situaciones, los evaluadores deben asumir que todo el software contiene algunos (aunque disimulada) errores

## 😃 **Pruebas de caja de cristal**

-   Se basan en el flujo del programa.
-   Prueba todos los caminos posibles de una función. Ramificaciones, bucles for y while, recursión.
-   Sirve para *regression testing* o *mocks*. Esto es, cuando ya se liberó el programa pero descubrimos un bug que queremos arreglar.
    -   *if:* Debemos probar todas las condiciones.
    -   *for* y *recursión:* Una donde no entre, otro donde entre una vez y otra donde entre varias.
    -   *while:* Donde la condición de entrada sea falsa y otra donde probemos los *break statements.*
-   También debemos probar todas las excepciones.

**import** unittest

**def** **es_mayor_de_edad**(edad):

**if** edad \>= 18:

**return** **True**

**else**:

**return** **False**

**class** **PruebaDeCristalTest**(unittest.TestCase):

**def** **test_es_mayor_de_edad**(self):

edad = 20

resultado = es_mayor_de_edad(edad)

self.assertEqual(resultado, **True**)

**def** **test_es_menor_de_edad**(self):

edad = 16

resultado = es_mayor_de_edad(edad)

self.assertEqual(resultado, **False**)

**if** \__name_\_ == '__main__':

unittest.ma

## **Verbosity=2 al método unittest.main**

**if** \__name_\_ == '__main__':

unittest.main(verbosity=2)

Se le puede agregar el parámetro verbosity=2 al método unittest.main para que el resultado en la consola sea mas detallado.

## **Excepciones comunes:**

ImportError : una importación falla;

IndexError : una lista se indexa con un número fuera de rango;

NameError : se usa una variable desconocida ;

SyntaxError : el código no se puede analizar correctamente

TypeError : se llama a una función en un valor de un tipo inapropiado;

ValueError : se llama a una función en un valor del tipo correcto, pero con un valor inapropiado

## **Manejo de excepciones**

Los manejos de excepciones son muy comunes en la programación, no tienen nada de excepcional. Las excepciones de Python normalmente se relacionan con errores de semántica, también podemos crear nuestras propias excepciones, pero cuando una excepción no se maneja (*unhandled exception*), el programa termina en error.

Las excepciones se manejan con los keywords: try, except, finally. Se pueden utilizar también para *ramificar* programas.

No deben manejarse de manera silenciosa (por ejemplo, con print statements). Para crear tu propia excepción utiliza el keyword *raise*.

"""Creamos una función en donde cada elemento de

una lista es dividida por un divisor definido"""

**def** **divide_elementos_de_lista**(lista, divisor):

"""El programa intentara realizar la división"""

**try**:

**return** [i / divisor **for** i **in** lista]

"""En caso de error de tipo ZeroDivisionError que

significa error al dividir en cero, el programa

ejecutara la siguiente instrucción"""

**except** ZeroDivisionError **as** e:

**return** lista

lista = list(range(10))

divisor = 0

print(divide_elementos_de_lista(lista, divisor))

import math

\#raiz cuadrada

*def* raiz_cuadrada_elementos_lista(*lista*, *multiplicador*):

try:

return [math.sqrt(i\*multiplicador) for i in lista]

except *ValueError* as e:

print (e)

return *f*'no existe la raíz cuadrada de un negativo'

lista = *list*(range(10))

multiplicador = -8

print (raiz_cuadrada_elementos_lista(lista, multiplicador))

# **Excepciones y control de flujo**

Hasta ahora hemos visto como las excepciones nos permiten controlar los posibles errores que pueden ocurrir en nuestro código. Sin embargo, dentro de la comunidad de Python tienen otro uso: control de flujo.

En este momento ya debes estar familiarizado con las estructuras de control flujo que ofrece Python (if... elif...else); entonces, ¿por qué es necesaria otra modalidad para controlar el flujo? Una razón muy específica: el principio EAFP (*easier to ask for forgiveness than permission*, es más fácil pedir perdón que permiso, por sus siglas en inglés).

El principio EAFP es un estilo de programación común en Python en el cual se asumen llaves, índices o atributos válidos y se captura la excepción si la suposición resulta ser falsa. Es importante resaltar que otros lenguajes de programación favorecen el principio LBYL (*look before you leap*, revisa antes de saltar) en el cual el código verifica de manera explícita las precondiciones antes de realizar llamadas.

Veamos ambos estilos:

\# Python

**def** **busca_pais**(paises, pais):

\&quot;&quot;&quot;

Paises es un diccionario. Pais es la llave.

Codigo con el principio EAFP.

\&quot;&quot;&quot;

**try**:

**return** paises[pais]

**except** KeyError:

**return** **None**

// Javascript

/\*\*

\* Paises es un objeto. Pais es la llave.

\* Codigo con el principio LBYL.

\*/

**function** **buscaPais**(paises, pais) {

**if**(!Object.keys(paises).includes(pais)) {

**return** **null**;

}

**return** paises[pais];

}

Como puedes ver, el código de Python accede directamente a la llave y únicamente si dicho acceso falla, entonces se captura la excepción y se provee el código necesario. En el caso de JavaScript, se verifica primero que la llave exista en el objeto y únicamente con posterioridad se accede.

Es importante resaltar que ambos estilos pueden utilizarse en Python, pero el estilo EAFP es mucho más "pythonico".

