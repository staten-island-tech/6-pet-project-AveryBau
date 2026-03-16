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

""" class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory
    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

Jillian = Hero("Jillian", 150, ["potion"])
Jillian.buy({"title": "Sword", "atk": 34})
print(Jillian.__dict__) """

""" class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def show_balance(self):
        print(f"{self.owner} has ${self.balance}")

sophie = BankAccount("Sophie", 41)
sophie.deposit({"amount": 67})
print(sophie.__dict__) """


class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory
    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

Sophie = Hero("Sophie", 676767, ["Doomscroll"])
Sophie.buy({"title": "Brainrot", "atk": 41})
print(Sophie.__dict__)

class Pet:
    def __init__(self, name, happiness):
        self.name = name
        self.__happiness = happiness
    def play(self, time):
        self.happiness += time
    def show_status(self):
        print(f"{self.name} is {self.__happiness}")

Dog = Pet("Bark", 1)
Dog.play(int(time = 9))
print(Dog.__dict__)
