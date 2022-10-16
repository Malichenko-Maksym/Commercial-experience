# Ввід даних користувачем, що до довжини інтервалу і кількості точок, де потрібно знайти значення функції
min_of_range = float(input("Range will start at: "))
max_of_range = float(input("Range will end at: "))
number_of_checkpoints = int(input("Number of checkpoints: "))
# Відстань між пунктами 
checkpoint_frequency  = (max_of_range - min_of_range) / number_of_checkpoints
# Функція, що знаходить значення даної математичної функції у визначеному пункті
def math_function(x):
    return x/(x+1) if (x+1)!=0 else " don't exist "
#Створення ''шапки'' таблиці
print("x".center(18), "function`s value".center(25), "accurate function`s value".center(30), "accurancy".center(14), "iteration number".center(18))
# Цикл, що знаходить усі точки, де потрібно обчислити функцію
for i in range(number_of_checkpoints):
    current_point = min_of_range + (checkpoint_frequency*i)
# форматоване виведення даних, з резервацією місця
    print(str(current_point).center(18), str(math_function(current_point)).center(25), str(math_function(current_point)).center(30), "|up_to_10^-16|".center(14), str(i+1).center(18))
    
input()