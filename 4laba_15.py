cars_number = int(input("Number of cars: "))
cars = []
sumary_price = 0
old_cars = 0
# Введення інформації про автомобілі
# Дані будемо зберігати у масиві з кортежів
# Кортеж двочисловий: перше число відповідає за ціну машини, а друге за її вік
for car in range(cars_number):
    price = int(input("Car price is "))
    age = int(input("Car age is "))
# Дані про старі машини збираємо одразу
    if age > 6: 
        sumary_price+=price
        old_cars+=1
    cars.append((price,age))
# Виведення інформації щодо усіх автомобілей
print(cars)
# Виведення інформації щодо середньої ціни автомобілів, що є старшими 6 років
print("avarage price of cars older then 6 years: ",sumary_price/old_cars)