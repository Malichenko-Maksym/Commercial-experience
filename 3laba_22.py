import re
# Створюємо словник голосних
vowels = { "a":False, "e":False, "i":False, "o":False, "u":False, "y":False}
text = input("Enter your text: ")
# Перебираємо текст, якщо знаходимо голосну, зазначаємо, що вона є в тексті
for char in text:
    if (char in vowels.keys()) and  (re.search(char,text)):
        vowels[char]=True
# Виведення відповіді
answer = []
for key in vowels:
    if vowels[key]==True:
        answer.append(key)

print(answer)
