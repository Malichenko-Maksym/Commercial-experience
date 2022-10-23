import random

         
#Створюємо списки, задаємо їх параметри
list_given = []
list_odd = [] #список для непарних
list_even  = [] #список для парних
min_elem = int(input("Min elemet is "))
max_elem = int(input("Max elemet is "))
n_elem_in_given_list = int(input("How many elements given list has? "))

#заповнюємо  список випадковими числами, згідно з заданими параметрами
for index in range(0,n_elem_in_given_list):
    elem = random.randint(min_elem,max_elem)
    list_given.append(elem)

#візуалізація спискy
print("given list : ", list_given)

#оголошуємо змінну логічного типу, що вказуватиме нам на парність позиції елемента
#проходимося по всьому заданому масиву ''розкидуючи'' його елементи по двох кошиках,
#в залежності від значення змінної
odd_turn = True
for element in list_given:
    if odd_turn:
        list_odd.append(element)
    else:
        list_even.append(element)
    odd_turn = not odd_turn

#Кінцевий результат
print("odd list : ", list_odd)
print("even list : ", list_even)




