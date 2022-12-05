from datetime import datetime
# Napiste metodu is_expired, ktera vrati pokud je jidlo prosle
# Jidlo bude prosle pokud datetime.now bude > nez datetime jidla
# Pokud bude prosle tak vratite True, jinak False
# fridge.add_food(Food('blue cheese', 40, datetime(2022, 6, 12)))

class Food:
    def __init__(self, name, price, expired) -> None:
        self.name = name
        self.price = price
        self.expired = expired

    def is_expired(self):
        return self.expired > datetime.now()

    def __repr__(self) -> str:
        return f'Food:: name: {self.name}, price: {self.price}, expired:{self.expired}'


class Fridge:
    def __init__(self) -> None:
        self.content = []

    def add_food(self, food: Food):
        if food.expired is False:
            self.content.append(food)
            return True
        return False

    def add_foods(self, *foods: Food):
        for food in foods:
            if food.expired is True:
                return False
        for food in foods:
            self.content.append(food)
        return True

    def get_price(self):
        sum_price = 0
        for food in self.content:
            sum_price += food.price
        return sum_price

    def __repr__(self) -> str:
        return str(self.content)


fridge = Fridge()
print(fridge)

fridge.add_food(Food('blue cheese', 40, datetime(2022, 6, 12)))
fridge.add_food(Food('milk', 20, datetime(2022, 4, 12)))

print(fridge)
# for food in fridge.content:
#    print(food)
