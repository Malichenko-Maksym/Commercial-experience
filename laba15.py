# Математична залежність
# Бачимо, що кожне наступне число основи виразу (n) в знаменнику менше на 1 за попереднє
# Тож все що нам потрабно зробити, це обрахувати значення для n=1, 
# Всі решта значення n будуть знаходитися рекуренційно: 
# наприклад, щоб знайти значення для n=3: потрібно знайти значення для n=2, 
# а його знайдемо (значення для n=2) знаючи значення n=1

def mathematical_dependence(n):
    if n < 1:
        return 'Imposible to calculate value, given number must be a positive integer'
    elif n == 1:
        return 1/(1+(1/2))
    else: 
        return 1/(n+mathematical_dependence(n-1))

given_number=int(input("Your number: "))
print("Given mathematical dependence : ", end="")
print(mathematical_dependence(given_number))