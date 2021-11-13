# Arreglos en Python


## Crear arreglos
***

Los arreglos en Python se delimitan con corchetes, de la siguiente manera:

    myArray = []

Pueden ser inicializados ingresando los valores directamente entre los corchetes separados por comas, los items de un arreglo pueden ser de distintos tipos:

- Numeros enteros
- String
- Booleanos
- Números flotantes
- Diccionarios
- Otros arreglos

Ejemplo: 

    myInitializedArray = [1, 2, 3, 'Cuarto', 'Quinto', True, {'dic1': 'Elemento del diccionario'}, ['Another Array']]


## Acceder a los arreglos
***

El acceso a los arreglos se puede hacer por medio de posiciones, estas como en la mayoria de los lenguajes de programación inician en 0

    myFirstItem = myInitializadArray[0]
    print(myFirstItem)

En Python se tiene la posibilidad de utilizar indices negativos, lo cual hará que se obtengan las ultimas posiciones del arreglo

    myLastItem = myInitializedArray[-1]
    print(myLastItem)


## Obtener subarreglos
***

También se pueden obtener subarreglos a partir de un arreglo existente, por ejemplo, con el arreglo *myInitializedArray* si se quisiera obtener solo el subarreglo [1, 2, 3] se puede hacer de la siguiente manera:
    
    myArrayPart = myInitializedArray[0:3]
    print( myArrayPart )

La sintaxis es la siguiente:

    Arreglo + corchete de abertura + posición de inicio del subarreglo + dos puntos + posición de fin del subarreglo + corchete de cierre

La posición de fin del subarreglo es la posición donde ya NO se tomarán los elementos, por lo tanto, la sintaxis [0:3] obtendra los elementos 0, 1 y 2, al llegar a la posición 3 el subarreglo se finalizá y esa posición ya no se incluye en el subarreglo.

De igual manera se pueden usar subarreglos con posiciones negativas, por ejemplo:

    myArrayFinishPart = myInitializedArray[-3:]
    print( myArrayFinishPart )

Este ejemplo obtendrá los ultimos 3 elementos del arreglo, los dos puntos sin una posición indican que será hasta la ultima posición del arreglo, incluyendo el ultimo elemento, esto obtendrá como resultado el subarreglo [True, {'dic1': 'Elemento del diccionario'}, ['Another Array']]

De igual manera que los dos puntos sin posición al final representan el fin del arreglo, se pueden usar dos puntos al sin posición al inicio, lo cual indica que se obtendrá desde la primer posición del arreglo, sin embargo, esto en ocasiones puede ser confuso:

    myArrayPart = myInitializedArray[0:3]
    print( myArrayPart )

Este ejemplo es igual que el subArray[0:3] del primer ejemplo.

## Obtener subarreglos con salto de elementos
***

Otra propiedad interesante para obtener subarreglos es que se puede modificar la frecuencia para obtener elementos del arreglo, por ejemplo, por defecto el subarreglo tomará todos los elementos en el rango que se especifique, pero esto se puede alterar para que tome un elemento por cada 2, 3 o cualquier numero de elementos, por ejemplo:

    subarray = myInitializedArray[::2]
    print(subarray)

Este ejemplo dará como resultado el subarreglo [1, 3, 'Quinto', {'dic1': 'Elemento del diccionario'}], correspondiente a los elementos con posición par del arreglo (posiciones 0, 2, 4 y 6 del arreglo), para obtener los elementos de posiciones impares se puede utilizar el parametro de inicio del subarreglo:

    subarray = myInitializedArray[1::2]
    print(subarray)

De igual manera, se puede cambiar el 2 por otro numero entero positivo, indicando que se tomará un elemento por cada 3, 4 o cualquier intervalo que se indique.

## Manipular elementos de un arreglo
***

Los arreglos pueden ser alterados durante la ejecución del programa, script o rutina que se este programando, ya que, a diferencia de las tuplas, estos son estructuras de datos manipulables.

Para agregar elementos al final del arreglo se utiliza el metodo *.append()*