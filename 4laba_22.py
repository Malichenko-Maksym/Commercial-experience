students = {}
students_number = int(input("Number of students students: "))
max_grades = 0
max_student_name = ''
# Введення інформації про студентів
for student in range(students_number):
    name = input("Student's name is ")
    g1 = int(input("Grade 1: "))
    g2 = int(input("Grade 2: "))
    g3 = int(input("Grade 3: "))
    g4 = int(input("Grade 4: "))
    # вираховування найкращого учня відьувається під час введення
    if g1+g2+g3+g4 > max_grades: 
        max_grades= g1+g2+g3+g4 
        max_student_name = name
    # дані про учнів зберігаємо у словнику, де ключем є прізвище учня,
    # а значенням кортеж з чьотирьох його оцінок
    students[name] = (g1,g2,g3,g4)
# Виведення словника
print(students)
#  Виведення посортованих даних зі словника (сортуємо прізвище, за алфавітом)
for key in sorted(students):
    print(key,": ", students[key])
# Оголошення найкращого учня 
print("The best student is: ", max_student_name)
    




