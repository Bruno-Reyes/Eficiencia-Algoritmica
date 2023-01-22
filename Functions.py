#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 21:41:04 2022

@author: brunorg
"""
import random



# ============================================

# Se genera el arreglo que se usara para realizar las pruebas
n = []
tam_n = 10
for i in range(0,50):
    elementos = []
    for j in range(tam_n):
        elementos.append(random.randint(1, 100))
    print(elementos)
    n.append(elementos)
    tam_n += 10

# ============================================
"""
==================================
Bubble
==================================
"""

def ord_burbuja(arreglo):
    n = len(arreglo)

    for i in range(n-1):       # <-- bucle padre
        for j in range(n-1-i): # <-- bucle hijo
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
             
                
"""
Modo de uso:
"""

# print("Antes de ordenarlo: ")
# print(elementos)
# ord_burbuja(elementos)
# print("Después de ordenarlo: ")
# print(elementos)
""" =============================================================== """


"""
==================================
Quick-Sort
==================================
"""
def sort(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        #print(izquierda+["-"]+centro+["-"]+derecha)
        return sort(izquierda)+centro+sort(derecha)
    else:
      return lista

"""
Modo de uso:
"""

# print("Antes de ordenarlo: ")
# print(elementos)
# quicksort(elementos)
# print("Después de ordenarlo: ")
# print(elementos)
# ===============================================================

"""
==================================
 Merge-Sort
==================================
"""

# Función merge_sort
def merge_sort(lista):
 
   if len(lista) < 2:
      return lista
    
    # De lo contrario, se divide en 2
   else:
        middle = len(lista) // 2
        right = merge_sort(lista[:middle])
        left = merge_sort(lista[middle:])
        return merge(right, left)
    
# Función merge
def merge(lista1, lista2):
    """
    merge se encargara de intercalar los elementos de las dos
    divisiones.
    """
    i, j = 0, 0 # Variables de incremento
    result = [] # Lista de resultado
 
   # Intercalar ordenadamente
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            result.append(lista1[i])
            i += 1
        else:
            result.append(lista2[j])
            j += 1
   # Agregamos los resultados a la lista
    result += lista1[i:]
    result += lista2[j:]
    # Retornamos el resultados
    return result

"""
Modo de uso:
"""

print("Antes de ordenarlo:")
print(elementos)
print("Después de ordenarlo:")
merge_sort_result = merge_sort(elementos)  
print(merge_sort_result)
# ===============================================================

