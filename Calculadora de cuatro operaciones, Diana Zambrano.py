# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 05:03:58 2008

@author: DIANA ZAMBRANO
"""
#Tarea 2: Crear una calculadora.

print("Bienveniendo a su calculadora básica, en el cual podrá obtener: \n Suma \n Resta \n División \n Multiplicación ")
print("\n Por favor, ingrese dos números:")
num1=int(input("Número 1:"))
num2=int(input("Número 2:"))
opcion=input("Seleccione la operación a realizar:\n\
             a=Suma\n\
             s=Resta\n\
             d=División\n\
             m=Multiplicación\n")

opcion=opcion.lower()    
res=0  
if opcion=="a":
    res=num1+num2
if opcion=="s":
    res=num1-num2
if opcion=="d":
    if num2!=0:
        res=num1/num2
if opcion=="m":
    res=num1*num2
else:
    print("\n No ha seleccionado una operación de las indicadas")
    num=0
print(f"\n Su resultado es:{res}")
