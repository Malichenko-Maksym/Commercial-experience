import re
#Створюємо словник голосних
vowels = { "a":0, "e":0, "i":0, "o":0, "u":0, "y":0}
text = input("Enter your text: ")
#За допомогою регулярних виразів розбиваємо текст на окремі слова
words = re.split('\W+', text)
#Знаходимо найдовше слово
longest_word = max(words, key=len)
#Рахуємо голосні у слові
for char in longest_word:
    if char in vowels:
        vowels[char]+=1
# Виводимо голосні на екран
for key in vowels:
    if vowels[key]>0:
        print(key,": ",vowels[key])
# Видаляємо найдовше слово
print(text.replace(longest_word,""))