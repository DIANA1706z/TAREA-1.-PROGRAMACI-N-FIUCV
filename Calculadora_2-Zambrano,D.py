# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 12:51:04 2008

@author: Diana Zambrano
"""

print("Welcome to your calculator \nHere you can to solver mathematicals operation")

#Operations:
op1 = "Suma"
op2 = "Resta"
op3 = "Multiplicación"
op4 = "División"
op5 = "El cuadrado de un número"
op6 = "Salir"
print('\nThe operations are:')
print(f'Opción1:{op1} \nOpción2:{op2} \nOpción3:{op3} \nOpción4:{op4} \nOpción5:{op5} \nOpción6:{op6}')

opción = 0
while (opción!=1):
    op = int(input('Please you select an operation:'))
    
    if op == 1:
       num1 = float(input('Insert the first number:'))
       num2 = float(input('Insert the second number:'))
       result= num1+num2
       print(f"Your result is:{result}")
       
       opt1 = 'Si'
       opt2 = 'No'
       
       while (opción!=2):
           opt = int(input('¿Quiere hacer otra operación con este resultado? \nSI: Inserte 1 \nNO:Inserte 2 \n'))
       
           if opt == 1:
               s = int(input('Seleccione una operación:'))
               if s == 1:
                   num3 = float(input('Insert the number:'))
                   result1 = result+num3
                   print(result1) 
               elif s == 2:
                   num3 = float(input('Insert the number:'))
                   result2 = result-num3
                   print(result2)
               elif s == 3:
                   num3 = float(input('Insert the number:'))
                   result3 = result*num3
                   print(result3)
               elif s == 4:
                   num3 = float(input('Insert the number:'))
                   result4 = result/num3
                   print(result4)
               elif s == 5:
                   result5 = result*result
                   print(result5)
               else :
                   print ('Operación Inválida')
           
           elif opt == 2:
               print('Operación terminada')
               break
        
           else:
               print('Operación inválida')
               break
            
               
              
    elif op == 2:
        num1 = float(input('Insert the first number:'))
        num2 = float(input('Insert the second number:'))
        result= num1-num2
        print(f"Your result is:{result}")
       
        opt1 = 'Si'
        opt2 = 'No'
        
        while (opción!=2):
           opt = int(input('¿Quiere hacer otra operación con este resultado? \nSI: Inserte 1 \nNO:Inserte 2 \n'))
       
           if opt == 1:
               s = int(input('Seleccione una operación:'))
               if s == 1:
                   num3 = float(input('Insert the number:'))
                   result1 = result+num3
                   print(result1) 
               elif s == 2:
                   num3 = float(input('Insert the number:'))
                   result2 = result-num3
                   print(result2)
               elif s == 3:
                   num3 = float(input('Insert the number:'))
                   result3 = result*num3
                   print(result3)
               elif s == 4:
                   num3 = float(input('Insert the number:'))
                   result4 = result/num3
                   print(result4)
               elif s == 5:
                   result5 = result*result
                   print(result5)
               else :
                   print ('Operación Inválida')
           
           elif opt == 2:
               print('Operación terminada')
               break
        
           else:
               print('Operación inválida')
               break

    elif op == 3:
        num1 = float(input('Insert the first number:'))
        num2 = float(input('Insert the second number:'))
        result= num1*num2
        print(f"Your result is:{result}")
       
        opt1 = 'Si'
        opt2 = 'No'
        
        while (opción!=2):
           opt = int(input('¿Quiere hacer otra operación con este resultado? \nSI: Inserte 1 \nNO:Inserte 2 \n'))
       
           if opt == 1:
               s = int(input('Seleccione una operación:'))
               if s == 1:
                   num3 = float(input('Insert the number:'))
                   result1 = result+num3
                   print(result1) 
               elif s == 2:
                   num3 = float(input('Insert the number:'))
                   result2 = result-num3
                   print(result2)
               elif s == 3:
                   num3 = float(input('Insert the number:'))
                   result3 = result*num3
                   print(result3)
               elif s == 4:
                   num3 = float(input('Insert the number:'))
                   result4 = result/num3
                   print(result4)
               elif s == 5:
                   result5 = result*result
                   print(result5)
               else :
                   print ('Operación Inválida')
           
           elif opt == 2:
               print('Operación terminada')
               break
        
           else:
               print('Operación inválida')
               break

    elif op == 4:
        num1 = float(input('Insert the first number:'))
        num2 = float(input('Insert the second number:'))
        result= num1/num2
        print(f"Your result is:{result}")
       
        opt1 = 'Si'
        opt2 = 'No'
        
        while (opción!=2):
           opt = int(input('¿Quiere hacer otra operación con este resultado? \nSI: Inserte 1 \nNO:Inserte 2 \n'))
       
           if opt == 1:
               s = int(input('Seleccione una operación:'))
               if s == 1:
                   num3 = float(input('Insert the number:'))
                   result1 = result+num3
                   print(result1) 
               elif s == 2:
                   num3 = float(input('Insert the number:'))
                   result2 = result-num3
                   print(result2)
               elif s == 3:
                   num3 = float(input('Insert the number:'))
                   result3 = result*num3
                   print(result3)
               elif s == 4:
                   num3 = float(input('Insert the number:'))
                   result4 = result/num3
                   print(result4)
               elif s == 5:
                   result5 = result*result
                   print(result5)
               else :
                   print ('Operación Inválida')
           
           elif opt == 2:
               print('Operación terminada')
               break
        
           else:
               print('Operación inválida')
               break
    
    elif op == 5:
        num1 = float(input('Insert the number:'))
        result= num1*num1
        print(f"Your result is:{result}")
       
        opt1 = 'Si'
        opt2 = 'No'
        
        while (opción!=2):
           opt = int(input('¿Quiere hacer otra operación con este resultado? \nSI: Inserte 1 \nNO:Inserte 2 \n'))
       
           if opt == 1:
               s = int(input('Seleccione una operación:'))
               if s == 1:
                   num3 = float(input('Insert the number:'))
                   result1 = result+num3
                   print(result1) 
               elif s == 2:
                   num3 = float(input('Insert the number:'))
                   result2 = result-num3
                   print(result2)
               elif s == 3:
                   num3 = float(input('Insert the number:'))
                   result3 = result*num3
                   print(result3)
               elif s == 4:
                   num3 = float(input('Insert the number:'))
                   result4 = result/num3
                   print(result4)
               elif s == 5:
                   result5 = result*result
                   print(result5)
               else :
                   print ('Operación Inválida')
           
           elif opt == 2:
               print('Operación terminada')
               break
        
           else:
               print('Operación inválida')
               
    
    elif op == 6:
        break
    else:
        print('Invalid Operation')
        break