""" class Calculator():
    def add(x, y):
        print(x + y)
        return x + y
    def add_many(numbers):
        print((sum(numbers)))
        return sum(numbers)
    def subtact(numbers):
        return numbers
Calculator.add(5, 6) """

class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory
    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

Jillian = Hero("Jillian", 150, ["potion"])
Jillian.buy({"title": "Sword", "atk": 34})
print(Jillian.__dict__)