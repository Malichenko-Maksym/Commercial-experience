import random
#функція що повертає перше неспівпадіння у списках (списки подаємо попередньо відсортовані)
def only_in_first( first_array, second_array):
    for elem in first_array:
        if elem not in second_array: return elem
    return False
         
#Створюємо списки, задаємо їх параметри
list1 = []
list2 = []
min_elem = int(input("Min elemet is "))
max_elem = int(input("Max elemet is "))
n_elem_in_first_list = int(input("How many elements first list has? "))
n_elem_in_second_list = int(input("How many elements second list has? "))
#заповнюємо обидва списки випадковими числами, згідно з заданими параметрами
for i in range(0,n_elem_in_first_list):
    elem1 = random.randint(min_elem,max_elem)
    list1.append(elem1)
for j in range(0,n_elem_in_second_list ):
    elem2 = random.randint(min_elem,max_elem)
    list2.append(elem2)
#сортування списків
list1.sort()
list2.sort()
#візуалізація списків
print("First list (sorted): ", list1)
print("Second list (sorted): ", list2)
#Кінцевий результат
if only_in_first(list1,list2):
    print("Minimal unique number from first list: ", only_in_first(list1,list2))
else:
    print("None such number exist")


