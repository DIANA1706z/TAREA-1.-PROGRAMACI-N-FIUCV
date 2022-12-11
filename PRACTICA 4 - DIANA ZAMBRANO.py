# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 14:27:08 2008

@author: DIANA ZAMBRANO
"""
print("Welcome")

#EJERCICIO 1

cadena_1= str(input("Insert a word:\n"))
cadena_2= str(input("Insert other word:\n"))
len(cadena_1)
len(cadena_2)
sorted(cadena_1)
sorted(cadena_2)

def esAnagrama(cadena_1,cadena_2):
    return sorted(cadena_1) == sorted(cadena_2)

if len(cadena_1) == len(cadena_2):
    print("Las palabras tienen el mismo tamaño.")

if sorted(cadena_1) == sorted(cadena_2):
    print("True, es un Anagrama.")
else:
    print("False, no es un Anagrama.")

#EJERCICIO 2

cadena_3= str(input("Inserte una oración:\n"))

len(cadena_3)

cadena_3 = cadena_3.lower()
split_oración = cadena_3.split()
primera_palabra = split_oración[0][0]

for i in range (1,len(split_oración)):
    individual_palabra = split_oración[i]
    if (individual_palabra[0]!=primera_palabra):
        print("false")
    else:
        print("true")
        print("Es un Tautograma")