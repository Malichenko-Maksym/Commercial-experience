class Drug:
    price_usd = 20
    name = "berlipryl"
    produser_country = "Germany"
# метод підвищує ціну препарата на 5 доларів
    def raise_price(self):
        self.price_usd = self.price_usd +5
# метод змінює країну виробництва
    def replace_production(self,new_country):
        self.produser_country = new_country

# Створення об'єктів на підставі класа
drug1 = Drug()
drug2 = Drug()
# Маніпуляція атрибутами
drug1.raise_price()
drug2.replace_production("Ukraine")
# Виведення інформації
print("price: ",drug1.price_usd," production country: ",drug1.produser_country)
print("price: ",drug2.price_usd," production country: ",drug2.produser_country)
