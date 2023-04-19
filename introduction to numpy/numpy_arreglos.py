# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

#arrays
a = np.array([1, 2, 3])
print("1D array: ", a)
b = np.array([(1, 2, 3), (1, 2, 3)])
print("3D array")
print(b)

#suma de matrizes rango
L1 = np.arange(10)
L2 = np.arange(10)
result = L1 + L2
print(result)

#matriz llena de unos de ixj
unos = np.ones((3,4)) # si fuera de ceros seria .zeros
print(unos)

aleatorios = np.random.random((2, 2))
print(aleatorios)

vacia = np.empty((3,2))
print(vacia)

full = np.full((4,5), 6)
print(full)

#una matriz del 0-30 con espaciado 5
espacio1 = np.arange(0, 30, 5)
print(espacio1)

#5 elementos entre el 0 y el 2
espacio2 = np.linspace(0,2,5)
print(espacio2)

"""
Crear matriz identidad
"""

identidad = np.identity(4)
print(identidad)


"""
Conocer las propiedades de una matriz
"""
#numero de filas
print(identidad.ndim)

#dimensiones de la matriz
print(identidad.shape)

#tipo de dato de la matriz
print(identidad.dtype)

#cambiar de tamaño una matriz
a=np.array([(1,2,3), (3,4,5)])
a = a.reshape(3,2)
print(a)