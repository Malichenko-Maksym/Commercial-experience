import random
import numpy as np
         
#Створюємо списки, задаємо їх параметри
matrix = []
#Зважаючи на максимально можливий елемент,
# і стовпчик, котрий точно братиме участь у перестановці (навідь сам з собою)
min_elem = 10 # будь-який елемент буде менше-рівний цього початкового значення
swap_column = 0

row_in_given_list = int(input("How many rows given list has? "))
column_in_given_list = int(input("How many colums given list has? "))
#заповнюємо  список випадковими числами, згідно з заданими параметрами
#Стовпчик де знаходиться мінімальний елемент запам'ятовуємо одразу, щоб не перебирати повторно список
for row in range(0,row_in_given_list):

    insert_list = []
    for column in range(0,column_in_given_list):
        elem = random.uniform(-10,10)
        if abs(elem) < min_elem:
            min_elem = abs(elem)
            swap_column = column
        insert_list.append(elem)
    matrix.append(insert_list)
# скористаймося можливостями бібліотеки НамПай
array = np.array(matrix)
#візуалізація спискy початкового
print(" Given list : ")
print(array)
# Власне кажучи, заміна стовпчиків
# Без бібліотеки довелося б або створювати допоміжний масив (буфер) для заміни стовпчиків
# Або замінювати 'Арифметичним способом' (додавання та відніміння значень у відповідних клітинках)
array[:, [swap_column, 0]] = array[:, [0, swap_column]]
#візуалізація спискy кінцевого
print(" Final list : ")
print(array)






