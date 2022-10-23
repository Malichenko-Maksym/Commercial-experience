import random
import numpy as np
         
#Створюємо списки, задаємо їх параметри
matrix = []
#Одиниця - нейтральний елемент множення
result = 1 

row_in_given_list = int(input("How many rows given list has? "))
column_in_given_list = int(input("How many colums given list has? "))
#заповнюємо  список випадковими числами, згідно з заданими параметрами
for row in range(0,row_in_given_list):
    insert_list = []
    for column in range(0,column_in_given_list):
        elem = random.randint(-10,10)
        insert_list.append(elem)
    matrix.append(insert_list)
# скористаймося можливостями бібліотеки НамПай для крощої репрезентації даних
array = np.array(matrix)
#візуалізація спискy початкового
print(" Given list : ")
print(array)

#Потрібно перебрати тільки елементи першого стовпчику
for row in range(0,row_in_given_list):
    if (matrix[row][0]<0) and (matrix[row][0]%2==0):  #перевірка умов парності на від'ємності
        result = result * matrix[row][0]
    
# 1- непарне число, так що якщо в кінці-кінців ми отримаємо одниницю, то це означатиме,
# що жодного множення не відбулося
if result!=1:
    print("Final result: ",result)
else:
    print("There weren't any negative even numbers in the first column")






