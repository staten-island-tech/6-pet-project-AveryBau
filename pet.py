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


""" class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory
    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

Sophie = Hero("Sophie", 676767, ["Doomscroll"])
Sophie.buy({"title": "Brainrot", "atk": 41})
print(Sophie.__dict__) """

""" class Pet:
    def __init__(self, name, happiness):
        self.name = name
        self.__happiness = happiness
    def play(self, play):
        self.__happiness += int(play)
    def show_status(self):
        print(f"{self.name} is {self.__happiness}")

Doggy = Pet("Barky Bark Bark", 10)
Doggy.play(play = 100)
print(Doggy.__dict__)

class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.__money = money
        self.__inventory = inventory
    def spend(self, item):
        self.__inventory.append(item)
    def egg (self, spend):
        self.__money -= int(spend)
    def yeah(self):
        print(f"{self.name} has {self.__money}")
Sabrina = Hero("Sabrina", 1234, ["Yuri"])
Sabrina.egg(spend = 67)
Sabrina.spend("MORE YURI")
print(Sabrina.__dict__)


class User: 
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"

class Student(User):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)
        self.student_id = student_id
    
    def display_info(self):
        return f"Student: {self.name}, Email:{self.email}, Student ID: {self.student_id}"
    
class Teacher(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject
    
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Subject: {self.subject}"
        return f"teacher: {self.name}, Email: {self.email}, Subject: {self.subject}"
    
class Administrator(User):
    def __init__(self, name, email, role):
        super().__init__(name, email)
        self.role = role

    def display_info(self):
        return f"Administrator: {self.name}, Email: {self.email}, Role: {self.role}"
    
    def manage_system(self):
        return f"{self.name} ({self.role}) is managing the vote"
    

student = Student("Alice", "alice@example.com", "S12345")
teacher = Teacher("Mr. Smith", "smith@example.com", "Mathematics")
administrator = Administrator("Ms. Johnson", "johnson@example.com", "Principal")

print(student.display_info())
print(teacher.display_info())
print(administrator.display_info())

admin = Administrator("Ms. Johnson", "johnson@example.com", "Principal")
print(admin.manage_system())

my_teacher = Teacher("Mr. Smith", "smith@example.com", "Mathematics")
print(my_teacher.display_info())
 """


import random   
class Pet:
    def __init__(self, name, clean = 100, hunger = 100, happiness = 100, age = 1, living = True):
        self.name = name
        self.clean = clean
        self.hunger = hunger
        self.happiness = happiness
        self.age = age 
        self.living = living
    def statSelf(self):
        self.clean -= 10
        self.happiness -= 15
        self.hunger -= 20
    def aging(self):
        self.age += 1 
    def warnings(self):
        if self.hunger <= 30:
            print(f"{self.name} is really, really hungry")
        elif self.hunger >= 85:
            print(f"{self.name} is full!")
        if self.happiness <= 30:
            print(f"{self.name} is unhappy and is growing a sense of hatred towards you")
        elif self.happiness >= 85:
            print(f"{self.name} is so happy!")
        if self.clean <= 30:
            print(f"{self.name} is very dirty and smelly")
        elif self.clean >= 85:
            print(f"{self.name} is nice and clean!")
    def impact_1(self):
        cat.clean = 100
    def impact_2(self):
         cat.happiness += 50
    def impact_3(self):
         cat.hunger = 100
         
class player:
    def __init__(self, name):
        self.Username = name
   
print("Welcome! You are getting a new cat! All you gotta do is keep your cat alive. Good luck!")
Userinput = input("What's your name? ")
USER = player(Userinput)
Userinput = input("What is the cat's name? ")
cat = Pet(Userinput)
Userinput2 = True
 
print(f"Congrats on your first pet! Welcome home, {cat.name}!")
 
while cat.living == True:
    print(f"Rise and shine! Day: {cat.age}")
    cat.warnings()
    Userinput = input(f"What would you like to do? You can clean, feed, play with, or watch {cat.name}.")
    Userinput = Userinput.lower()
    if "clean" in Userinput:
            cat.impact_1
            cat.happiness -= 40
            cat.statSelf()
    elif "play" in Userinput:
            cat.impact_2
            cat.hunger -= 25
            cat.clean -= 50
            cat.statSelf()
    elif "feed" in Userinput:
            cat.impact_3
            cat.happiness += 50
            if cat.happiness > 100:
                cat.happiness = 100
            cat.statSelf()
    elif "watch" in Userinput:
            cat.statSelf()
    else:
            print("Sorry, invalid answer. Try again.")
    if cat.clean <= 0 or cat.happiness <= 0 or cat.hunger <= 0:
            cat.living = False
            break
    elif cat.clean <= 0 :
            cat.living = False
            print(f"{cat.name}'s hygiene was neglected")
            break
    elif cat.hunger <= 0 :
            cat.living = False
            print(f"{cat.name} starved")
            break
    elif cat.happiness <= 0 :
            cat.living = False
            print(f"{cat.name} is too unhappy")
            break
   
    print(f"Time for {cat.name} to go to bed!")
    print("It's your free time now!! ")
    Userinput2 = True
    
    while Userinput2 == True:
        print(f"You can check {cat.name}'s stats or sleep." )
        Userinput = input("What would you like to do? ")
        if "stats" in Userinput or cat.name in Userinput.lower():
                print(f"Hunger: {cat.hunger}, Cleanliness: {cat.clean}, Happiness: {cat.happiness}, Age: {cat.age} days")
                print(" ")
        elif "sleep" in Userinput: 
            print(f"Good night, {USER.Username}.... ")
            print(" ")
            Userinput2 = False
        else:
            print("Sorry, invalid answer. Try again. ")
            print(" ")
    
    cat.aging()
print(f"Uh oh... {cat.name} has died...")
print(f"Oops...")
Userinput = input(f"what...would you like...to do..?")
if "bury" in Userinput:
    print(f"You walk into the backyard. {cat.name} is getting heavy in your arms. A shovel lays on the ground.")
    print(f"You buried {cat.name}.")
else: 
    print(f"You feel very guilty for killing {cat.name}")
    print("You're traumatized and will never get a pet ever again")
    print("What have you done?")
