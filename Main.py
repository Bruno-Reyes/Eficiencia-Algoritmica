#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 21:18:47 2022

@author: brunorg
"""

# ------- Librerias -----------------------
from time import time_ns
import matplotlib.pyplot as plt
import numpy as np
import random
import math


"""
==================================
 Funcion a evaluar
==================================
"""

#### Cualquier funcion de python que se quiera evaluar. 

"""
==============================================================================

==============================================================================
"""

"""
 Funcion encargada de las mediciones del tiempo
"""
def medir_tiempo(function, A):
    Tn = []
    n = [] 
    for i in A:
        antes = time_ns()
        function(i)
        despues = time_ns()
        Tn.append(despues - antes)
        n.append(len(i))
    
    np.array(Tn)
    np.array(n)
    return (Tn,n)

# Ejecutamos la función a evaluar. 

Tn , iteraciones  = medir_tiempo(NombreDeLaFuncionAEvaluar)  


# ----------------------- Grafica -----------------------
# Instanciamos el estilo del plot
plt.style.use('ggplot')

# Definimos el tamaño de la letra

plt.plot(iteraciones, Tn, 'o--' ,linewidth=1.0, color='#e14658', markersize=1)
#plt.xticks(iteraciones)
#plt.yticks(Tn)
ax = plt.gca()
plt.title("Comportamiento del algoritmo")
plt.ylim(0,max(Tn))
plt.xlabel('n')
plt.ylabel('T(n)')
ax.set_facecolor('#22252c')
plt.grid()
plt.show()

# ----------------------- Coeficiente de correlacion -----------------------

# n : Numero de iteraciones
# x : Vector de valores en nanosegundos
# y : Vectores de familias con respecto a 'x'
# Numero de iteraciones
n = int(len(iteraciones))
# Calculando los vectores de las familias
y = {'Exponencial': [], 'Lineal': [], 'Constante' : [],'Logaritmica': [] }


for valor in Tn:
    # Exponencial y = x²
    y['Exponencial'].append(math.pow(valor,2))
    # Lineal y = x
    y['Lineal'].append(valor)
    #Constante y = c 
    y['Constante'].append(np.mean(Tn))
    # Logaritmica y = log(x)
    if valor != 0:
        y['Logaritmica'].append(math.log(valor,10))
    else: 
        y['Logaritmica'].append(0)

ccFamilia = {'Exponencial': 0, 'Lineal': 0, 'Constante' : 0,'Logaritmica': 0 }

for clave in y:
    Calculos = {'n*sum((x*y))':0 ,'sum(x)':0,'sum(y)':0,'sum(x)*sum(y)':0, 'n*sum(x^2)':0 , 'sum(x)^2':0,'n*sum(y^2)':0 , 'sum(y)^2':0 }
    # Calculando n* sum( x*y )
    for a , b in zip(Tn,y[clave]):
        Calculos['n*sum((x*y))']+= a*b
    Calculos['n*sum((x*y))'] = n*Calculos['n*sum((x*y))']

    # Calculando sum(x) * sum (y)
    for a , b in zip(Tn,y[clave]):
        Calculos['sum(x)']+= a
        Calculos['sum(y)']+= b

    Calculos['sum(x)*sum(y)'] = Calculos['sum(x)']*Calculos['sum(y)']

    # Calculando n * sum(x²)
    for a in Tn:
        Calculos['n*sum(x^2)']+= pow(a,2)
    Calculos['n*sum(x^2)'] = n*Calculos['n*sum(x^2)']

    # Calculando sum(x)²
    Calculos['sum(x)^2'] = pow(Calculos['sum(x)'],2)

    # Calculando n * sum(y²)
    for b in y[clave]:
        Calculos['n*sum(y^2)']+= pow(b,2)
    Calculos['n*sum(y^2)'] = n*Calculos['n*sum(y^2)']

    # Calculando sum(y)²
    Calculos['sum(y)^2'] = pow(Calculos['sum(y)'],2)
    
    numerador = Calculos['n*sum((x*y))']-Calculos['sum(x)*sum(y)']
    denominador = math.sqrt((Calculos['n*sum(x^2)']-Calculos['sum(x)^2'])*(Calculos['n*sum(y^2)']-Calculos['sum(y)^2']))
    #print(clave)
    #print(Calculos)
    
    
    if numerador==0 or denominador==0:
        ccFamilia[clave] = 0
    else: 
        ccFamilia[clave] = numerador/denominador
        


# Encontrar la familia a la que pertenece el algoritmo
pertenencia = ''
mejorValor = 0 
for clave in ccFamilia:
    if abs(ccFamilia[clave]) > mejorValor:
        mejorValor = abs(ccFamilia[clave])
        pertenencia = clave
print('Su algoritmo pertenece a la familia: '+pertenencia)

# ----------------------- Funciones para las notaciones -----------------------

def bigO(pertenencia, Tn, iteraciones):
    
    exp = []
    lin = []
    const = []
    log = []
    # Para la exponencial
    yi = 0 
    for i in Tn:
        if i != 0:
           yi = i
           break
    print('Modelo exponencial:')
    print('y = ('+str(yi)+'/'+str(iteraciones[0])+'^2'+')*'+'x^2\n')
    
    # Para la lineal
    # Calcular las pendientes
    pendientes = []
    for i in range(len(Tn)):
        pendientes.append(Tn[i]/iteraciones[i])
    print('Modelo lineal:')
    print('y = '+str(max(pendientes))+'x + 0\n')
    
    # Para el constante
    c = max(Tn)
    
    print('Modelo Constante:')
    print('y = '+str(c)+'\n')
    
    # Para el logaritmico
    coordLog = [iteraciones[pendientes.index(max(pendientes))], Tn[pendientes.index(max(pendientes))]]
    print('Modelo Logaritmico:')
    print('y = ('+str(coordLog[1])+'/log('+str(coordLog[1])+')'+')*'+'log(x)\n')
    
    for valor in iteraciones:
        # Exponencial
        exp.append((yi/iteraciones[0]**2)*(valor**2))
        # Lineal
        lin.append(valor*max(pendientes))
        # Constante
        const.append(c)
        # Logaritmo
        if valor != 0:
            log.append((coordLog[1]/math.log(coordLog[0],10))*(math.log(valor,10)))
        else: 
            log.append(0)
    return (exp, lin, const, log)

def littleO(pertenencia, Tn, iteraciones):
    exp = []
    lin = []
    const = []
    log = []
    # Para la exponencial
    yi = 0 
    for i in Tn:
        if i != 0:
           yi = i
           break
       
    yi += 1
    print('Modelo exponencial:')
    print('y = ('+str(yi)+'/'+str(iteraciones[0])+'^2'+')*'+'x^2\n')
    
    # Para la lineal
    # Calcular las pendientes
    pendientes = []
    for i in range(len(Tn)):
        pendientes.append(Tn[i]/iteraciones[i])
    print('Modelo lineal:')
    print('y = '+str(max(pendientes)+1)+'x + 0\n')
    
    # Para el constante
    c = max(Tn)+1
    
    print('Modelo Constante:')
    print('y = '+str(c)+'\n')
    
    # Para el logaritmico
    coordLog = [iteraciones[pendientes.index(max(pendientes))]+1, Tn[pendientes.index(max(pendientes))]+1]
    print('Modelo Logaritmico:')
    print('y = ('+str(coordLog[1])+'/log('+str(coordLog[1])+')'+')*'+'log(x)\n')
    
    for valor in iteraciones:
        # Exponencial
        exp.append((yi/iteraciones[0]**2)*(valor**2))
        # Lineal
        lin.append(valor*(max(pendientes)+1))
        # Constante
        const.append(c)
        # Logaritmo
        if valor != 0:
            log.append((coordLog[1]/math.log(coordLog[0],10))*(math.log(valor,10)))
        else: 
            log.append(0)
    return (exp, lin, const, log)

def bigOmega(pertenencia, Tn, iteraciones):
    
    exp = []
    lin = []
    const = []
    log = []
    # Para la exponencial
    yi = Tn[-1]

    print('Modelo exponencial:')
    print('y = ('+str(yi)+'/'+str(iteraciones[-1])+'^2'+')*'+'x^2\n')
    
    # Para la lineal
    # Calcular las pendientes
    pendientes = []
    for i in range(len(Tn)):
        pendientes.append(Tn[i]/iteraciones[i])
        
    m = max(pendientes)
    for i in pendientes: 
        if i != 0 and i < m:
            m = i
    
    print('Modelo lineal:')
    
    print('y = '+str(m)+'x + 0\n')
    
    # Para el constante
    minTn = max(Tn)
    for i in Tn: 
        if i != 0 and i < minTn:
            minTn = i
    c = minTn
    
    print('Modelo Constante:')
    print('y = '+str(c)+'\n')
    
    # Para el logaritmico
    coordLog = [iteraciones[pendientes.index(m)], Tn[pendientes.index(m)]]
    print('Modelo Logaritmico:')
    print('y = ('+str(coordLog[1])+'/log('+str(coordLog[1])+')'+')*'+'log(x)\n')
    
    for valor in iteraciones:
        # Exponencial
        exp.append((yi/iteraciones[-1]**2)*(valor**2))
        # Lineal
        lin.append(valor*m)
        # Constante
        const.append(c)
        # Logaritmo
        if valor != 0:
            log.append((coordLog[1]/math.log(coordLog[0],10))*(math.log(valor,10)))
        else: 
            log.append(0)
    return (exp, lin, const, log)

def littleOmega(pertenencia, Tn, iteraciones):
    
    exp = []
    lin = []
    const = []
    log = []
    # Para la exponencial
    yi = Tn[-1]

    print('Modelo exponencial:')
    print('y = ('+str(yi)+'/'+str(iteraciones[-1])+'^2'+')*'+'x^2  -1\n')
    
    # Para la lineal
    # Calcular las pendientes
    pendientes = []
    for i in range(len(Tn)):
        pendientes.append(Tn[i]/iteraciones[i])
        
    m = max(pendientes)
    for i in pendientes: 
        if i != 0 and i < m:
            m = i
    
    print('Modelo lineal:')
    
    print('y = '+str(m)+'x + 0 - 1\n')
    
    # Para el constante
    minTn = max(Tn)
    for i in Tn: 
        if i != 0 and i < minTn:
            minTn = i
    c = minTn
    
    print('Modelo Constante:')
    print('y = '+str(c)+' -1 \n')
    
    # Para el logaritmico
    coordLog = [iteraciones[pendientes.index(m)], Tn[pendientes.index(m)]]
    print('Modelo Logaritmico:')
    print('y = ('+str(coordLog[1])+'/log('+str(coordLog[1])+')'+')*'+'log(x) - 1\n')
    
    for valor in iteraciones:
        # Exponencial
        exp.append(((yi/iteraciones[-1]**2)*(valor**2))-1)
        # Lineal
        lin.append((valor*m)-1)
        # Constante
        const.append(c-1)
        # Logaritmo
        if valor != 0:
            log.append(((coordLog[1]/math.log(coordLog[0],10))*(math.log(valor,10)))-1)
        else: 
            log.append(0)
    return (exp, lin, const, log)

def thetha(pertenencia, Tn, iteraciones):
    (exp1, lin1, const1, log1) = bigO(pertenencia, Tn, iteraciones)
    (exp2, lin2, const2, log2) = bigOmega(pertenencia, Tn, iteraciones)
    
    return (exp1, exp2, lin1, lin2, const1, const2, log1, log2)
# Preguntar la notacion asintotica en la que se desea representar
notacion = int(input('¿Que notacion asintotica desea visualizar?\n 1. Big o\n 2. Little o\n 3. Big omega\n 4. Little omega\n 5. Thetha\n ?'))
title = ''

if notacion==1: 
    (exp, lin, const, log) = bigO(pertenencia, Tn, iteraciones)
    title = 'Big O'

if notacion==2: 
    (exp, lin, const, log) = littleO(pertenencia, Tn, iteraciones)
    title = 'Little O'
    
if notacion==3: 
    (exp, lin, const, log) = bigOmega(pertenencia, Tn, iteraciones)
    title = 'Big Omega'
    
if notacion==4: 
    (exp, lin, const, log) = littleOmega(pertenencia, Tn, iteraciones)
    title = 'Little Omega'
    

# ----------------------- Grafica con notacion -----------

if notacion != 5:
    # Instanciamos el estilo del plot
    plt.style.use('ggplot')

    # Definimos el tamaño de la letra

    plt.plot(iteraciones, Tn, 'o--' ,linewidth=1.0, color='#e14658', markersize=1)
    plt.plot(iteraciones, exp, linewidth=1.0, color='#03FEDD',markersize=1, label = 'Exponencial')
    plt.plot(iteraciones, lin, linewidth=1.0, color='#FE9603',markersize=1, label = 'Lineal')
    plt.plot(iteraciones, const, linewidth=1.0, color='#037BFE',markersize=1, label = 'Constante')
    plt.plot(iteraciones, log, linewidth=1.0, color='#9D03FE',markersize=1, label = 'Logaritmo')
    ax = plt.gca()
    plt.title("Notacion "+str(title))
    plt.ylim(0-(Tn[-1]/10),max(Tn)+(Tn[-1]/10))
    plt.xlabel('n')
    plt.ylabel('T(n)')
    plt.legend()
    ax.set_facecolor('#22252c')
    plt.grid()
    plt.show()

else: 
    
    
    (exp1, exp2, lin1, lin2, const1, const2, log1, log2) = thetha(pertenencia, Tn, iteraciones)
    title = 'Thetha'
    
    # Instanciamos el estilo del plot
    plt.style.use('ggplot')

    # Definimos el tamaño de la letra

    plt.plot(iteraciones, Tn, 'o--' ,linewidth=1.0, color='#e14658', markersize=1)
    plt.plot(iteraciones, exp1, linewidth=1.0, color='#03FEDD',markersize=1)
    plt.plot(iteraciones, exp2, linewidth=1.0, color='#03FEDD',markersize=1)
    plt.plot(iteraciones, lin1, linewidth=1.0, color='#FE9603',markersize=1)
    plt.plot(iteraciones, lin2, linewidth=1.0, color='#FE9603',markersize=1)
    plt.plot(iteraciones, const1, linewidth=1.0, color='#037BFE',markersize=1)
    plt.plot(iteraciones, const2, linewidth=1.0, color='#037BFE',markersize=1)
    plt.plot(iteraciones, log1, linewidth=1.0, color='#9D03FE',markersize=1)
    plt.plot(iteraciones, log2, linewidth=1.0, color='#9D03FE',markersize=1)
    ax = plt.gca()
    plt.title("Notacion "+str(title))
    plt.ylim(0-(Tn[-1]/10),max(Tn)+(Tn[-1]/10))
    plt.xlabel('n')
    plt.ylabel('T(n)')
    ax.set_facecolor('#22252c')
    plt.grid()
    plt.show()
