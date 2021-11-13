
# Arreglo vacio
myArray = []

# Arreglo inicializado
myInitializedArray = [1, 2, 3, 'Cuarto', 'Quinto', True, {'dic1': 'Elemento del diccionario'}, ['Another Array']]

""" # Acceso a elementos por posiciones
myFirstElement = myInitializedArray[0]
print( myFirstElement )
myLastElement = myInitializedArray[-1]
print( myLastElement ) """


""" # Obtener subarreglos
subarray = myInitializedArray[0:3]
print( subarray )
subarray = myInitializedArray[-3:]
print( subarray )
subarray = myInitializedArray[:3]
print(subarray) """


""" # Obtener subarreglos con salto de elementos
subarray = myInitializedArray[::2]
print(subarray) """


# Manipular arreglos ya inicializados

""" #Insertar al final
myArray.append('MyItem')
myArray.append('Other item')
print( myArray )

# Insertar en una posición especifica
myArray.insert(0, 'New item')
myArray.insert(1, 'second item')
print( myArray )

# Clonar un arreglo
myEqualArray = myArray
myCloneArray = myArray.copy()
print(myEqualArray)
print(myCloneArray)

# Eliminar elemento al final de un arreglo
myArray.pop()

# Eliminar elemento especifico de un arreglo
myArray.remove('New item')
print(myArray)
print(myEqualArray)
print(myCloneArray)

# Limpiar un arreglo
myArray.clear()
print( myArray )

# Contar repeticiones de x elemento en el arreglo
myCloneArray.append('New item')
elements = myCloneArray.count('New item')
print(elements)

# Unir arreglos
myOtherarray = [1, 2, 3]
myCloneArray.extend(myOtherarray)
print(myCloneArray)

# Obtener indice de un item, solo toma la primer coincidencia
print( myCloneArray.index('New item') )

# Invertir el arreglo
myCloneArray.reverse()
print( myCloneArray )

# Ordenar el arreglo (El arreglo debe ser del mismo tipo)
myIntArray = [12, 45, 23, 1, 8, 234, 7, 34]
myIntArray.sort()
print( myIntArray )
myIntArray.sort(reverse=True)
print(myIntArray) """

# Recorrer arreglos

# for in
for element in myInitializedArray:
    print(element)

# for con indice
for index in range(len(myInitializedArray)):
    print(index, ": ", myInitializedArray[index])