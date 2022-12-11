# -*- coding: utf-8 -*-
"""
Spyder Editor: Diana Zambrano

This is a temporary script file.
"""
print("Se tiene una lista y se pide ordenar en forma ascendente y descendente")
n=[10,15,54,27,36,47]
print(n)
#print(len(n))

#Comparar los números

#Escoger el primer lugar de la lista:
print(n[0])
print(n[1])

if n[0] < n[1]:
    print("10 is less than 15")
if n[0] < n[2]:
    print("10 is less than 54")
if n[0] < n[3]:
    print("10 is less than 27")
if n[0] < n[4]:
    print("10 is less than 36")
if n[0] < n[5]:
    print("10 is less than 47")

print("the first in the list n is:",n[0])


#Escoger el segundo lugar de la lista:
if n[1] < n[2]:
    print("15 is less than 54")
if n[1] < n[3]:
    print("15 is less than 27")
if n[1] < n[4]:
    print("15 is less than 36")
if n[1] < n[5]:
    print("15 is less than 47")
    
print("the second in the list is:")
print(n[1])

#Escoger el tercer lugar de la lista:
if n[2] < n[3]:
    print("54 is less than 27")
if n[2] < n[4]:
    print("54 is less than 36")
if n[2] < n[5]:
    print("54 is less than 47")
    
    if n[2] > n[0]:
        print("54 is bigger than 10")
    if n[2] > n[1]:
        print("54 is bigger than 15")
        
        if n[3] < n[2]:
            print("27 is less than 54")
        if n[3] < n[4]:
            print("27 is less than 36")
        if n[3] < n[5]:
            print("27 is less than 47")
    
print("the third in the list is:",n[3])

#Escoger el cuarto lugar de la lista:
if n[2] < n[3]:
    print("54 is less than 27")
if n[2] < n[4]:
    print("54 is less than 36")
if n[2] < n[5]:
    print("54 is less than 47")
    
    if n[4] < n[2]:
            print("36 is less than 54")
    if n[4] < n[5]:
            print("36 is less than 47")
        
print("the fourth in the list is:",n[4])

#Escoger el quinto lugar de la lista:
if n[2] < n[3]:
    print("54 is less than 27")
if n[2] < n[4]:
    print("54 is less than 36")
if n[2] < n[5]:
    print("54 is less than 47")
    
    if n[5] < n[2]:
            print("47 is less than 54")
    if n[5] > n[4]:
            print("47 is bigger than 36")

print("the fifth in the list is:",n[5])

#Como queda un solo numero sería el ultimo de la lista.
if n[2] > n[0]:
    print("true")
if n[2] > n[1]:
    print("true")
if n[2] > n[3]:
    print("true")
if n[2] > n[4]:
    print("true")
if n[2] > n[5]:
    print("true")
print("the sixth in the list is:",n[2])

#Lista Ascendente:
n_asc=[10,15,27,36,47,54]
print(n_asc)

print("___________________________________________")


#Escoger el primer lugar de la lista:
if n[5] > n[0]:
    print("47 > 10")
if n[5] > n[1]:
    print("47 > 15")
if n[5] > n[2]:
    print("47 > 54")
if n[5] > n[3]:
    print("47 > 27")
if n[5] > n[4]:
    print("47 > 36")

    if n[2] > n[0]:
        print("54 > 10")
    if n[2] > n[1]:
        print("54 > 15")
    if n[2] > n[3]:
        print("54 > 27")
    if n[2] > n[4]:
        print("54 > 36")
    if n[2] > n[5]:
        print("54 > 47")
print("the first in the list is:",n[2])


#Escoger el segundo lugar de la lista:
if n[4] > n[0]:
    print("36 > 10")
if n[4] > n[1]:
    print("36 > 15")
if n[4] > n[3]:
    print("36 > 27")
if n[4] > n[5]:
    print("36 > 47")

    if n[4] < n[5]:
        print("36 < 47")
    if n[4] < n[2]:
        print("36 < 54")
  
print("the second in the list is:",n[5])


#Escoger el tercer lugar de la lista:
if n[3] > n[0]:
    print("27 > 10")
if n[3] > n[1]:
    print("27 > 15")
if n[3] > n[4]:
    print("27 > 36")

    if n[3] < n[4]:
        print("27 < 36")
    if n[3] < n[5]:
        print("27 < 47")
  
print("the third in the list is:",n[4])

#Escoger el cuarto lugar:
if n[3] > n[0]:
    print("27 > 10")
if n[3] > n[1]:
    print("27 > 15")
if n[3] > n[4]:
    print("27 > 36")

    if n[3] < n[4]:
        print("27 < 36")
    if n[3] < n[5]:
        print("27 < 47")
    if n[3] < n[2]:
        print("27 < 54")
  
print("the fourth in the list is:",n[3])   

#Escoger el quinto lugar:
if n[1] > n[0]:
    print("15 > 10")
   
    if n[1] < n[2]:
        print("15 < 54")
    if n[1] < n[3]:
        print("15 < 27")
    if n[1] < n[4]:
        print("15 < 36")
print("the fifth in the list is:",n[1])  

#Como queda un número por descarte
#este sera el último de la lista. 
if n[0] < n[1]:
    print("10 < 15")
    
print("the sixth in the list is:",n[0])


#Lista Descendente:
n_desc=[54,47,36,27,15,10]
print(n_desc)



