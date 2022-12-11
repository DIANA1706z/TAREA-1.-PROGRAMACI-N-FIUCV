# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 03:17:23 2008

@author: Diana Zambrano
"""
#Ejercicio1

N=int(input("Ingrese un número mayor a uno:\n"))

fib_list=[1,1]


if N < 1:
    print("El número ingresado no es valido.")
else:
    while fib_list[-1] < N:
        fib_list.append(fib_list[-2]+fib_list[-1])

if fib_list[-1] > N:
    fib_list.pop(-1)
    print("La serie de fibbionacci es:\n", fib_list)
else:
    print("La serie de Fibionacci es:\n", fib_list)
    

#Ejercicio 2

result=0

for i in fib_list:
    result = result+i
print("La suma de Fibionacci es:\n", result)


#Ejercicio 3

suma_impar = 0

for i in fib_list:
    if not i % 2 == 0:
        suma_impar = suma_impar + i
        
print("La suma de los impares de Fibionacci es:\n",suma_impar)


#Ejercicio 4

numero_primo=0

for i in fib_list:
    if i % 2 == 0:
        result=i
        print("El siguiente número de Fibionacci no es un número primo:",result)
    elif i / 1 == i:
        result_primo=i
        print("El número de Fibionacci es primo:\n",result_primo)
    else:
        print("No hay primos")