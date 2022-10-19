# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#%% 28.09.2022. 

"""
user_number = int(input("Give us the number: "))
for i in range(1, user_number,2):
    for j in range(i): 
        print("*")
                
    """


"""
# tribonacci numbers. 
def tri(number): 
    number1 = number2 = 1
    number3 = 2
    tribonacci = [number1, number2, number3]

    for i in range(3,number,3):
        number1 = number1 + number2 + number3
        number2 = number2 + number3 + number1
        number3 = number3 + number1 + number2
        tribonacci.append(number1)
        tribonacci.append(number2)
        tribonacci.append(number3)
    
    number = tribonacci[number-1]
        
    return number
        
print(tri(9))
"""



"""
def get_formatted_name(name, surname): 
    full_name = f"{name} {surname}"
    return full_name.title()

print(get_formatted_name("Alisher", "Temirlanov"))


while True: 
    first = input("Give us the first name: ")
    if first == "q": 
        break
    second = input("Give us the second name: ")
    if second == "q": 
        break
    print(get_formatted_name(first, second))
"""

"""
import numpy as np

a = np.array([[1,2,3]])
print(a)
print(a.shape)
"""


#%% 27.09.2022. 



"""# prime numbers
user_number = int(input("Give us a number: "))

numbers_values = []

for i in range(2, user_number): 
    if user_number % i == 0: 
        numbers_values.append(i)


if numbers_values: 
    print(f"{user_number} is not prime")
else: 
    print(f"{user_number} is prime")

"""
#%% 25.09.2022. 


"""
element1 = [1,2,3]
element2 = [1,2]
def trans(items): 
    head, *tail = items
    return head + sum(tail) if tail else head

print(trans(element1))
print(trans(element2))
"""

"""some_list = [[1,2,3], [4,5,6], [7,8,9], [10,11,12,13]]
for i in some_list: 
    for n in i: 
        print(n)
"""


"""
#working with records of 3 types

records = [
    ("full", "John", 24, "CS"),
    ("full", "Michael", 25, "Business"), 
    ("partial", "Nike", "Finance"), 
    ("partial", "Nancy", "Law"),
    ]

def full(x,y,z): 
    info = ("\nThe full info is: "+
            f"\nThe name: {x}"+
            f"\nThe age: {y}"+
            f"\nThe major: {z}")
    print(info)

def partial(x,y): 
    info = ("\nThe partial info is: "+
            f"\nThe name: {x}"+
            f"\nThe major: {y}")
    print(info)

for typee, *details in records: 
    if typee == "full": 
        full(*details)
    else: 
        partial(*details)

"""


# practicing with *
"""
user_info = {
    "name": "John",
    "age": 25, 
    "class": "CS"    
    }


name, *other_info = user_info.values()
print(other_info)


records = [1,2,3,4,5,6,7,8,9,10]

firsst_record, *many_records, key_records = records
print(many_records)
"""

"""import json

# function that greets users

def greet_user(): 
    
    try: 
        with open("username.txt") as f: 
            username = json.load(f)
    except FileNotFoundError: 
        username = input("What is your name? ")
        with open("username.txt", "w") as f: 
            json.dump(username, f)    
        print(f"We'll remember your name, dear {username}!")
    else: 
        print(f"Welcome back, dear {username}")

greet_user()
"""


"""import json

numbers = [1,2,3,4,5,6,7,8,9,10, 100, 1000]

filename = "numbers.json"
with open(filename, "w") as f: 
    json.dump(numbers, f)
    
with open(filename) as f: 
    the_numbers = json.load(f)

print(the_numbers)
"""



"""
filename = "some_story.txt"
with open(filename) as f:
    contents = f.read()

word = "the"
print(contents.lower().count(word))
"""

"""
def count_words(file_name): 
    try: 
        with open(file_name) as f: 
            contents = f.read()
    except FileNotFoundError: 
        print(f"Sorry, the file {file_name} doesn't seem to exist.")
    else: 
        words = contents.split()
        num_words = len(words)
        print(f"The {file_name} has {num_words} words.")
    
count_words("cats.txt")
count_words("dogs.txt")
count_words("undefined.txt")
"""


"""
try: 
    f1 = "cats.txt"
    f2 = "dogs.txt"
    f3 = "undefined.txt"

    file1 = open(f1, "r")
    file2 = open(f2, "r")
    file3 = open(f3, "r")
    print(file3)
    print(file3.read())
except FileNotFoundError: 
    print(f"The document {f3} doesn't exist")


print("These are cats: ")
print(file1.read())
print("These are dogs: ")
print(file2.read())
print("And this file doesn't exsit: ")
"""

"""
filename = "dogs.txt"
file = open(filename, "w")
file.write("John\nMark\nBob")

file.close()
"""

"""
filename = "cats.txt"

file = open(filename, "r")
for i in file: 
    print(i)
file.close()

file = open(filename, "r")
print(file.read())

"""
"""
# friendly calculator

print("Let's add 2 numbers and see the sum!")
while True:     
    try:
        number1 = int(input("Please, enter the first number: "))
        break
    except ValueError: 
        print("Please, only numbers!")
while True:
    try: 
        number2 = int(input("Please, enter the second number: "))
        break
    except ValueError: 
        print("Please, only numbers!")

sum = number1 + number2
print(f"The sum is {sum}")
"""


#%% 23.09.2022. 
"""
# split
some_phrase = "Hey, mister Tat, how are you! You look great today!"
print(some_phrase.split(" "))
print(some_phrase.split(","))
print(some_phrase.split("!"))
print(some_phrase.split("  "))
print(some_phrase)

some_phrase1 = some_phrase.split(" ")
"""
"""
# learning exceptions

number = 100
try: 
    number = number / 0
except ZeroDivisionError: 
    print("No division by zero!")

try: 
    user = int(input("give us a number: "))
except ValueError: 
    print("Only numbers, please!")
else: 
    print(f"Your number is {user}")
    
"""
"""
# working with files

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(f"{pi_string[:52]}...")
print(len(pi_string))
"""

#%% 22.09.2022. 

# lottery
"""
from random import choice

some_list = ["a", "b", "c", "d", "e"]

for i in range(1,11): 
    some_list.append(i)
    
successful_picks = ["a", 3]
times = 0
while successful_picks: 
    number = choice(some_list)
    if number in successful_picks: 
        print("Hey, you won the lottery!")
        successful_picks.remove(number)
    else: 
        print("Good luck next time!")
        some_list.remove(number)
    times += 1

print(f"It took you {times} times to win the lottery!")
"""
"""
from random import choice

some_list = ["a", "b", "c", "d", "e"]

for i in range(1,11): 
    some_list.append(i)

print(some_list)
successful_picks = ["a", 3]
for i in range(1,4): 
    number = choice(some_list)
    if number in successful_picks: 
        print("Hey! You won the lottery!")
    else: 
        print("Good luck next time!")


# how many times to win the lottery?
print("")
i = 0
while successful_picks in some_list: 
    number = choice(some_list)
    if number in successful_picks: 
        print("Hey! You won the lottery!")
        some_list.remove(number)
    else: 
        some_list.remove(number)
        print("Good luck next time!")
    i += 1

print(f"It took you {i} times to win the lottery twice!")
"""
"""

# working with dice 
from random import randint, choice

class Die: 
    def __init__(self, sides=6): 
        self.sides = sides

    def roll_die(self): 
        return randint(1, self.sides)

die6 = Die()
for i in range(1,11): 
    print(f"{i}) {die6.roll_die()}")

print("")
die10 = Die(10)
for i in range(1,11): 
    print(f"{i}) {die10.roll_die()}")

print("")
die20 = Die(20)
for i in range(1,11): 
    print(f"{i}) {die20.roll_die()}")
    

"""
"""
class Course: 
    def __init__(self, title, units): 
        self.title = title
        self.units = units
        
    def declare(self): 
        declaration = f"The course is {self.title} with {self.units} units."
        return declaration 


CS50 = Course("CS50", 100)
print(CS50.declare())

class Lecture(Course): 
    def __init__(self, title, units, difficulty):
        super().__init__(title, units)
        self.difficulty = difficulty
        
    def lecture(self): 
        declaration = f"The course {self.title} with {self.units} units has {self.difficulty} difficulty level."
        return declaration
    
CS = Lecture("CS50", 100, "high")
print(CS.lecture())

"""

#%% 21.09.2022. 

"""
# further work with classes
class User:
    def __init__(self, name, possibilities): 
        self.name = name
        self.possibilities = possibilities
        
    
class Admin(User): 
    def __init__(self, name, possibilities): 
        super().__init__(name, possibilities)

    def admin_possibilities(self): 
        result = ["Add users", "Remove users", "Delete Messages"]
        return result

"""

#%% 19.09.2022. 

"""
import pandas as pd 

data = {"name": ["Fuat", "Aukyt", "Erkut"], 
        "midterm": [60, 85, 100], 
        "final": [69, 90, 100], 
        "attendance": [6, 10, 10]
        }

df_ifs4203 = pd.DataFrame(data)
print(df_ifs4203.head())

"""
"""

import math

class Point:

    def __init__(self, x, y): 
        self.x = x
        self.y = y
        
    def setXY(self): 
        self.x = float(input("Please, set the attribute X: "))
        self.y = float(input("Please, set the attribute Y: "))
    
     
    def getXY(self):
        print(f"X is {self.x} and Y is {self.y}")

    
    def distance(self, point):
        return math.sqrt((point.y - self.y)**2 + (point.x - self.x)**2)
    
     
    def angle(self, point):
        return math.atan((point.y - self.y)/(point.x - self.x) * (180 / math.pi))

#5) 
P1 = Point(0.0, 0.0)
P2 = Point(5.0, 5.0)
P3 = Point(3.0, 4.0)
P4 = Point(6.0, 8.0)
print("\ndistance (1):")
print(P1.distance(P2))
print(P2.distance(P1))

print("\ndistance (2):")
print(P3.distance(P4))
print(P4.distance(P3))

print("\nangle (1):")
print(P1.angle(P2))
print(P2.angle(P1))

print("\nangle (2):")
print(P3.angle(P4))
print(P4.angle(P3))

"""


"""
""#%% 18.09.2022.


class Performance: 
    
    def __init__(self, name):
        self.name = name
        
    def performance_info(self, GPA): 
        info = f"The {self.name}'s GPA is {GPA}"
        return info
    
    
class Student: 
    
    def __init__(self, name, age): 
        self.name = name
        self.age = age
        self.year = ""
        self.academic_excellence = Performance(self.name)
        
    def student_info(self): 
        info = (f"Student's name {self.name} and they are {self.age} years old." + 
        f"They are {self.grade} students.")
        return info

    def Year(self): 
        print("Choose which year student are you: ")
        print("Select '1' if freshman"+"\nSelect '2' if sophomore"+
              "\nSelect '3' if junior"+"\nSelect '4' if senior")
        
        while True: 
            try:
                year = int(input("What year are you: "))
                if year not in [1,2,3,4]: 
                    print("Only years from '1' to '4', please!")
                    continue
                else: 
                    if year == 1: 
                        stud_type = "freshman"
                    elif year == 2:
                        stud_type = "sophomore"
                    elif year == 3:
                        stud_type = "junior"
                    else: 
                        stud_type = "senior"
                    print(f"Great! Your are a {stud_type} student!")
                    self.year = stud_type
                    break
            except ValueError: 
                print("Please, only numbers!")
            
                    
john = Student("John", 19)
john.Year()

"""
#%% 17.09.2022. 
"""
# one decent class with inheritance

class University: 
    
    def __init__(self, name, found, location, studs, level, tuition): 
        self.name = name
        self.foundation = found
        self.location = location
        self.students = studs
        self.level = level
        self.tuition = tuition
    
    def declaration(self): 
        result = (f"The organization's name is {self.name} "+
                  f"was founded in {self.foundation} "+
                  f"with {self.students} students "+
                  f"at {self.level} level, "+
                  f"paying {self.tuition} a year!")
        return result
    
harvard = University("Harvard", 1700, "East Coast", 20_000, "TOP", "50,000USD+")
print(harvard.declaration())


class College(University): 
    def __init__(self, name, found, location, studs, level, tuition): 
        super().__init__(name, found, location, studs, level, tuition)

hbs = College("Harvard Business School", 1700, "East Coast", 15_000, "TOP", "45,000USD+")
print("")
print(hbs.declaration())

"""

"""

# playing with classes

class SomeRandomClass: 
    def __init__(self, name, facts):
        self.name = name
        self.facts = facts
        self.fun_fact = ""
        
    def presentation(self): 
        return f"{self.name}'s facts are:"
    
    def funny_fact(self, funny_fact): 
        self.fun_fact = funny_fact
        
facts = ["born in 2000", "plays music instruments", "loves math"]
funny_fact = "doesn't know own age"
John = SomeRandomClass("John", facts)
print(John.presentation())
for i in John.facts: 
    print(i)

John.funny_fact(funny_fact)
print(John.fun_fact)

"""

"""
# with Sultan's help the final version

import math


class Point:
    x, y = 0, 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    #1) 
    def setXY(self, x, y):
        self.x = x
        self.y = y
    
    #2) 
    def getXY(self):
        print(f"X is {self.x} and Y is {self.y}")

    #3) 
    def distance(self, point):
        return math.sqrt((point.y - self.y)**2 + (point.x - self.x)**2)
    
    #4) 
    def angle(self, point):
        return math.atan((point.y - self.y)/(point.x - self.x) * (180 / math.pi))

#5) 
P1 = Point(0.0, 0.0)
P2 = Point(5.0, 5.0)
P3 = Point(3.0, 4.0)
P4 = Point(6.0, 8.0)
print("\ndistance (1):")
print(P1.distance(P2))
print(P2.distance(P1))

print("\ndistance (2):")
print(P3.distance(P4))
print(P4.distance(P3))

print("\nangle (1):")
print(P1.angle(P2))
print(P2.angle(P1))

print("\nangle (2):")
print(P3.angle(P4))
print(P4.angle(P3))

# second attempt to complete the home assignment

class Point: 
    x, y = 0, 0
    
    def __init__(self, x, y): 
        self.x = x
        self.y = y
        
    def setXY(self): 
        self.x = float(input("Please, set the attribute X: "))
        self.y = float(input("Please, set the attribute Y: "))
    
    def getXY(self): 
        print(f"X is {self.x} and Y is {self.y}")

    #def distance(self, point_b): 
     #   result = math.sqrt(())
      #  print(f"The Euclidean distance of 2 points is: ")
        

"""
"""
class Student: 
    def __init__(self, name, major, GPA): 
        self.name = name
        self.major = major
        self.GPA = GPA
        
    def info(self): 
        info = f"{self.name}'s major is {self.major} with GPA {self.GPA}"
        return info
        
studentA = Student("John McCartney", "Computer Science", 3.4)
print(studentA.info())
"""



#%% 15.09.2022. 

"""
class Company: 
    def __init__(self, name, users, level): 
        self.name = name
        self.users = users
        self.level = level
        self.revenue = 0
        
    def company_intro(self, mission): 
        intro1 = f"{self.name} has {self.users} with the following mission: "
        intro2 = mission
        return intro1 + intro2

apple = Company("Apple", 1_000_000_000, "Top")
apple.revenue = 350_000_000_000
apple_mission = "to bring the best user experience to its customers through its innovative hardware, software, and services"
print(apple.company_intro(apple_mission))
"""
"""
# restaurant class
class Restaurant: 
    
    def __init__(self, name, cuisine): 
        self.name = name
        self.cuisine = cuisine
        
    def describe_restaurant(self):
        print(f"The restaurant's name is {self.name}")
        print(f"It has {self.cuisine} cuisine")
        
    def open_restaurant(self): 
        print(f"The restaurant {self.name} is open! Welcome!")
    
assorti = Restaurant("Assorti", "Kazakh")
assorti.describe_restaurant()
assorti.open_restaurant()
print("")
mcdonalds = Restaurant("McDonalds", "American")
mcdonalds.describe_restaurant()
mcdonalds.open_restaurant()
"""

"""
# working with classes!

class People: 
    #A simple attempt to model a human-being
    
    def __init__(self, name, age): 
    #Initialize the name and age attributes.
        self.name = name
        self.age = age
        
    def live(self): 
        print(f"{self.name} is now alive.")
    
    def eat(self): 
        print(f"{self.name} is now eating food!")
        

person = People("Alisher", 24)
print(f"{person.name}'s age is {person.age}.")

person.live()
person.eat()


"""

#%% 14.09.2022. 

"""
# two functions: one that transfers and another one that prints
enemies = []
allies = []
enemies[:2] = "Russia", "China", "USA"

def foes(countries): 
    print("These countries are enemies: ")
    for country in countries: 
        print(country)

def diplomat(enemies, allies): 
    # transforms enemies into allies
    while enemies: 
        country = enemies.pop()
        allies.append(country)
        if country == "USA": 
            print(f"\nThis country {country} is no longer an enemy")
        else: 
            print(f"This country {country} is no longer an enemy")

def friends(countries): 
    print("\nThese countries are allies: ")
    for country in countries: 
        print(country)
        
foes(enemies)
diplomat(enemies, allies)
allies.sort(reverse = True)
friends(allies)
"""
"""
# functions and dictionaries
# let's get some info about someone

def info(name, surname, age=None): 
    person = {}
    person["name"] = name
    person["surname"] = surname
    if age: 
        person["age"] = age
    return person

for key, value in info("Alisher", "Temirlanov", 24).items(): 
    print(f"{key} is {value}")
"""
"""
# full_name ex.
def full_name(name, last_name, middle_name=""): 
    if middle_name: 
        print(f"The full name is {name} {middle_name} {last_name}")
    else: 
        print(f"The full name is {name} {last_name}")

name = input("What's your name: ")
last_name = input("What's your last name: ")
yes_no = input("Do you have middle name? Yes/No? ")
if yes_no == "yes": 
    middle_name = input("What's your middle name: ")

full_name(name, last_name, middle_name)
"""

"""
# multiple parameters
print("Multiple parameters function")
def multiple(a, b, c=5): 
    return (a+b-c)

print(multiple(1,2))
"""

"""
# working with functions

print("Working with Functions!")
def greeting(): 
    print("Hello, World!")

greeting()

#Ex 2.
print("Example 2.")
def interest(user, list_of_interests): 
    print(f"{user} has the following interests: ")
    for i in list_of_interests: 
        print(i)

user = input("What is your name? ")
interests = []
print("Tell us about your interests!")
while True: 
    user_input = input("To stop type 'stop': ")
    interests.append(user_input)
    if user_input == "stop": 
        break

interest(user, interests)

"""

"""
dream_vacations = {}

while True: 
    user_name = input("Tell us your name, please: ")
    vacation = input("Tell us where you'd like to go: ")
    
    dream_vacations[user_name] = vacation
    question = input("Is there anyone else left to fill the question? ")
    if question != "yes": 
        break

for person, dream in dream_vacations.items(): 
    print(f"{person}'s dream vacation is {dream}")
"""

"""
some_list = ["friends", "parents", "friends", "wife", "friends", "children"]

while "friends" in some_list: 
    print(some_list)
    some_list.remove("friends")
    
print(some_list)
"""


"""
# working with while and dictionaries

polling = {}
while True: 
    name = input("Tell us your name, please: ")
    age = int(input("What is your age now? "))
    
    polling[name] = age
    
    enough = input("Is there anyone else? 'Yes' or 'No' ")
    if enough == 'No': 
        break

    
for name, age in polling.items(): 
    print(f"{name}'s age is {age}")
"""

"""
ordered = []
finished = []
ordered[0:2] = "pizza", "juice", "free"

# aproach 1
while ordered: 
    for i in ordered:
        finished.append(i)
        print(f"I have prepared your {i}")
        
    del ordered[:]

# approach 2
ordered = []
finished = []
ordered[0:2] = "pizza", "juice", "free"

while ordered: 
    item = ordered.pop()
    finished.append(item)

finished.sort(reverse = True)
for i in finished: 
    if i == "pizza": 
        print(f"\nI have prepared your {i}")
    else:
        print(f"I have prepared your {i}")

"""
"""
# working with while loops.
user_input = ""

while user_input != 'quit': 
    user_input = input("(1) Say something and we will repeat it back: ")
    if user_input != 'quit': 
        print(user_input)
        print("Please, type 'quit' if you want to stop!")

    


# with flag (in this case active = True)
active = True
while active: 
    user_input = input("(2) Say something and we will repeat it back: ")
    if user_input == "quit": 
        active = False
    else: 
        print(user_input)
        print("Type 'quit' when you want to stop.")
 

# the only way to stop 'while  True' is break
while True: 
    user_input = input("(3) Say something and we will repeat it back: ")
    if user_input == 'quit': 
        break
    else: 
        print(user_input)
        print("Type 'quit' when you want to stop.")


# another example

user_input = ""

while user_input != 0: 
    user_input = int(input("(4) Give us a number and we will repeat it back: "))
    if user_input != 0: 
        print(user_input)
        print("Type '0' when you want to stop.")

# and last one:
some_list = list(range(0,11))
while len(some_list) !=0: 
    for i in range(0, len(some_list)): 
        if i % 2 == 0: 
            print(i)
            some_list.remove(i)
            print(some_list)
        else: 
            some_list.remove(i)
            print(some_list)
"""            
#%% 12.09.2022. 

"""
# exercises 2. 

# Task 1.
print("Task 1")
created_list = list(range(0,11))
for i in created_list:
    if i % 2 == 0: 
        print(i)

# Task 2.
print("\nTask 2")
def get_squares(input_list): 
    for i in input_list: 
        input_list[i] = i ** 2
    return input_list

print(get_squares(created_list))

# Task 3.
print("\nTask 3: Factorial")
def factorial_squared(n): 
    factorial_list = []
    odd_list = []
    for i in range(0,n+1): 
        factorial_list.append(i)
    for i in factorial_list: 
        i = i ** 2
    for i in factorial_list: 
        if i % 2 == 1: 
            odd_list.append(i)
    return odd_list
    
print(factorial_squared(15))

# Task 4.
print("\nTask 4")
def dictionary(n): 
    n_dictionary = {}
    for i in range(0, n): 
        n_dictionary[i] = i
    for key, value in n_dictionary.items():
        n_dictionary[value] = value ** 2 
    return n_dictionary

print(dictionary(10))

# Task 5.
print("\nTask 5")
list_dict = []
[print(i) for i in dictionary(10).keys()]

# Task 6.
print("\nTask 6")
user_number = 10
list_even = []
[list_even.append(i) for i in range(0, user_number) if i % 2 == 0]
print(list_even)



# Task 7. 
print("\nTask 7")
inch_listed = [4,4.5,5, 5.5, 6, 7]
#7.1.
def centimeters(inches_list): 
    cm_list = []
    for i in inches_list: 
        i = i * 2.54
        cm_list.append(i)        
    return cm_list

print(centimeters(inch_listed))

#7.2.
cm_listed = [i * 2.54 for i in inch_listed]
print(cm_listed)

#7.3.
def transfer(inches): 
    return inches * 2.54

map_list = map(transfer, inch_listed)
print(list(map_list))


# Task 8. 
print("\nTask 8")

"""

# lambda - mathematical function stimulation: 
"""
fun = lambda x,y,z: 2*x+z-y
print(fun(1,10,5))
"""
#%% 11.09.2022. 
# You have an N-element tuple or sequence that you would like to unpack into... 
#... a collection of N variables.
"""
def Avg(enter):
    avg = 0
    summa = 0
    for i in enter: 
        summa += i
    avg = summa/(len(enter))
    return avg


n1, n2, n3 = 1,2,3
n1, n2, n3 = n1+1,n2+2,n3+3+1
enter = [n1,n2,n3]

print(Avg(enter))
"""
"""

# introducing while loops. 
while True: 
    answer = "let's go home!"
    print(answer)
    if answer == "let's go home!": 
        break

current_number = 100
while current_number >= 0: 
    print(current_number)
    current_number -= 1

"""

"""
# working with user input. 
print("\nWorking with user input.")
print("")

user_name = input("Please, tell us your name: ")
print(f"User's name is '{user_name}'")

# making string to integer. 
question = "How old are you?"
question += "\tPlease, let us know! "
user_age = int(input(question))

if user_age >= 18: 
    print(f"\nDear {user_name}, you are allowed in the club!")
else: 
    print(f"\nDear {user_name}, sorry, you are not allowed in the club.")
"""


"""
print("finalizing with dictionaries")
countries = {"Kazakhstan": {"capital": "Astana", 
                            "population": 16_000_000, 
                            "language": "Kazakh"},
             "USA": {"population": 350_000_000, 
                     "language": "English", 
                     "currency": "USD"}, 
             "China": {"language": "Chinese", 
                       "currency": "Yuan", 
                       "populatoin": 1_300_000_000}
    }
for country, info in countries.items(): 
    print(f"\nThe country's name is {country}.")
    for detail, data in info.items(): 
        print(f"The {detail} of the {country} is {data}")
"""

"""
scientists = {
    "Einstein": 
        {"name": "Albert",
         "surname": "Einstein",
         "inventions": ["Theory of Relativity", "E=mc^2", "photoelectric theory"]},
    "Newton": {"name": "Isaac", 
               "surname": "Newton", 
               "inventions": ["First Law of Newton", "Second Law", "Third Law"]},
    "Tesla": {"name": "Nicola", 
              "surname": "Tesla",
              "inventions": ["Electrical Grid", "Terrestrial Startionary Waves", "Remote Control"]},
}



for scientist, info in scientists.items(): 
    print(f"\n{scientist}'s full name  is {info['name']} {info['surname']}.")
    print(f"{scientist}'s inventions are:")
    for invention in info["inventions"]: 
        print(invention)
"""



#%% 09.09.2022. 

"""
dictionary = {"a": {"b":"c"}}
print(dictionary["a"])

for keys, values in dictionary.items(): 
    for akeys, avalues in values.items(): 
        print(akeys, avalues)
"""


"""
scientists = {
    "Einstein": 
        {"name": "Albert",
         "surname": "Einstein",
         "inventions": ["Theory of Relativity", "E=mc^2", "photoelectric theory"]},
    "Newton": {"name": "Isaac", 
               "surname": "Newton", 
               "inventions": ["First Law of Newton", "Second Law", "Third Law"]},
    "Tesla": {"name": "Nicola", 
              "surname": "Tesla",
              "inventions": ["Electrical Grid", "Terrestrial Startionary Waves", "Remote Control"]},
}

for person, info in scientists.items(): 
    for details in info:
        print(f"{person}'s full name is ")
"""


#%% 08.09.2022. 

"""
persons = {
    ["Martin", "Aston"]: ["Cars", "Vehicles"],
    ["Michael", "Jackson"]: ["Music", "Dancing"],
    ["Steve", "Jobs"]: ["Apple", "Computers"]
    }

for key, value in persons.items(): 
    for i in key: 
        name = ""
        name += i
    for y in value: 
        hobby = ""
        hobby += y

print(f"{name}'s hobbies are: {hobby}")

"""
"""
# again, how to take stuff out of dictionaries. 
# first, dictionaries have keys and values. 
# thus, we should understand, what we want to get out of it
# if we need keys, then we should indicate it 

print("\nGetting keys:")
some_dict = {"place": "abc"}
if "placen" not in some_dict.keys(): 
    print("It doesn't have placeN")
if "place" in some_dict.keys(): 
    print("It has only place")

print("\nGetting values:")
some_dict = {"place": "abc"}
if "xyz" not in some_dict.values(): 
    print("It doesn't have XYZ")
if "abc" in some_dict.values(): 
    print("It has only ABC")    

"""
"""

# let's add some lists into dictionaries.
Bill_Gates = {
    "name": "William Gates III", 
    "age_category": "60+",
    "legacy": ["Microsoft", "Windows", "Gates Foundation"],
    }

Steve_Jobs = {
    "name": "Steven Paul Jobs",
    "age_category": "dead", 
    "legacy": ["Apple II", "Macintosh", "iPod", "iPhone", "Apple"]
    }

business_people = [Bill_Gates, Steve_Jobs]
for one in business_people: 
    if "legacy" in one: 
        print(f"\n{one['name']}'s legacy is in: ")
        for legacy in one['legacy']: 
            print(f"{legacy}")

"""
"""
# nesting as a powerful feature
master1 = {"Jeff Bezos": "Amazon CEO"}
master2 = {"Michael Jackson": "King of Pop"}
master3 = {"Bill Gates": "Microsoft"}
master4 = {"Steve Jobs": "Apple"}
masters = [master1, master2, master3, master4]
for master in masters: 
    for name, great in master.items(): 
        print(f"{name}'s achievement is {great}!")

# the next one was truly nice!
print("\nAll right, let's play with aliens in a big bigger numbers.")
aliens = []
for i in range(0, 100):
    alien = {"name": "alien"}
    aliens.append(alien)
    
for alien in aliens[:51]: 
    alien["name"]= "first half of aliens"

for alien in aliens[50:]: 
    alien["name"] = "second half of aliens"

for i in aliens: 
    for key, value in i.items(): 
        print(f"The {key} of the alien is {value}")
"""
"""
# looping through dictionaries while presenting information
person = {"name": "James", "age": 25, "location": "Apple City", 
          "hobby": "games", 
          "interests": "Computer Science"
          }

for key, value in person.items(): 
    print(f"Person's {key} is {value}")

    
# friends' favorite hobbies & interests
print("\n")
friends = {
    "Iliyas": "Football", 
    "Kirill": "Design", 
    "Sultan": "Music", 
    "Jeff": "Laughing"    
    }

for friend, hobby in friends.items(): 
    print(f"{friend}'s hobby is {hobby}")

# working only with keys or values
# btw, keys are default to be given:
print("\n")
for friend in friends: 
    print(f"Here are all the friends: {friend}")

# now with values
print("")
for hobby in friends.values(): 
    print(f"Here are all the hobbies: {hobby}")


# let's make them in a sorted way
print("\nSorted list of friends")
for friend, hobby in sorted(friends.items()): 
    print(f"{friend}'s hobby is {hobby}")

# set to pull out only unique values. 
print("")
favorite_programs = {
    "Bill Gates": "C", 
    "Steve Jobs": "Swift",
    "Richard Branson": "Virgin", 
    "Michael Jackson": "Swift", 
    "Jeff Bezos": "C"
    }

for fav_lang in sorted(set(favorite_programs.values())): 
    print(f"{fav_lang}")

"""
"""
# Working with dictionaries. {"a":"b"};
dictionary = {"word": "definition"}
print(dictionary["word"])

# Adding new items to the dictionary. 
dictionary["word1"]= "definition1"
print(dictionary)

print(f"The first word is {dictionary['word1']}")
dictionary["word1"] = "definitionN"
print(f"Now the first word is {dictionary['word1']}")
"""
"""
# working with aliens. 
alienA = {"name": "MrAlien", "position_A": "Almaty", "position_B": "Astana"}
if alienA["position_A"]=="Almaty": 
    print("You need to move to Astana")
    alienA["position_A"] += " to Astana"

if alienA["position_B"]=="Astana":
    print("You need to move to Almaty")
    alienA["position_B"] += " to Almaty"

print(alienA)

#removing key:value pairs
print("\n")
some_alien = {"name": "stranger", "age": 125, "extra_info": "XYZ"}
print(f"Here is info about the alien then: {some_alien}")
del some_alien["extra_info"]
print(f"Here is the info now: {some_alien}")

"""

#%%
"""
# some object applications

def fact1(n): 
    ans=1
    for i in range(2,n):
        ans = ans*i
    return ans

def fact2(n):
    if n<1: 
        return 1
    else: 
        return n * fact2(n-1)
    

print(fact1(6))
print(fact2(7))

"""

#%%
"""

from copy import deepcopy

# class assignment on 7.09.2022. 
#2) 
some_list = list(range(0,11))
print(some_list)

#3) 
print("\nTask 3")
a = ["I", "like", "cookies"]
b = a
b[2] = "apples"
print(a)
print(b)

#4) 
print("\nTask 4")
a = ["I", "like", "cookies"]
b = a[:]
b[2] = "apples"
print(a)
print(b)

#5)  
print("\nTask 5")
a = ["I", "like", ["chocolate", "cookies"]]
b = a[:]
b[2][1] = "apples"
print(a)
print(b)

#6) 
print("\nTask 6")
a = ["I", "like", ["chocolate", "cookies"]]
b = deepcopy(a)
b[2][1] = "apples"
print(a)
print(b)

"""
#%% 07.09.2022. 

"""
# working with logical operators if, elif, if-else
alphabet = ["a", "b", "c", "d", "E", "f"]
alphabet1 = alphabet
alphabet2 = ["z", "y", "x", "t", "u", "v"]
alphabet1 = alphabet1 + alphabet2

for i in alphabet1: 
    if i in alphabet: 
        print(f"{i} is in Alphabet")
    else: 
        print(f"{i} is not in Alphabet")

"""

#%%


"""
# checking whether subjects are available or not
available_subjects = ["Programming", "Big Data", "Economics", "Business", 
                      "Finance", "Management", "QA Testing"]

requested_subjects = ["Programming", "QA Testing"]
for i in requested_subjects: 
    if i in available_subjects: 
        print(f"The {i} course is available")
    else: 
        print(f"The {i} course is not available")

"""
#%%
"""
# age entrance example.         
print("\nAge Entrance Ex.")
age = int(input("What is your age? "))
price1 = 25
price2 = 50
price3 = 100

if age > 16 and age <= 18:
    print(f"The price is {price1}USD")
elif age > 18 and age <= 25: 
    print(f"The price is {price2}USD")
elif age > 25 and age <= 90: 
    print(f"The price is {price3}USD")
else: 
    print("The club is prohibited for you, sorry...")
    
    
"""
"""
# trying to pring stuff from a list to a simple sentence. unsuccessful yet.
l0 = ["I", "like", 20, "cookies", 21]
for i in l0: 
    i = str(i)

"""
"""
# playing with numbers and equations
number1 = 15
number2 = 35
print(number1>number2)
print(number1<number2)
numbers = [1,2,3,5,10,15,20,25,30,40]
print(number1 in numbers)
print(number2 not in numbers)
print((number1>number2)or(number1<number2))

"""

#%% 06.09.2022

"""
# if statements!
cities = ["Almaty", "Astana", "Taldykorgan", "Semey"]
for city in cities: 
    if city == "Astana": 
        print(f"This is the capital of Kazakhstan: {city}")
    else: 
        print(f"This is a gorgeous city of Kazakhstan: {city}")
"""
"""
# working with tuples - like lists but not changeable.
some_tuple = ("michael", "joseph", "jackson")
individual = [print(i.title()) for i in some_tuple]

"""
"""
# printing some parts of the lists. 
players = ["John", "Michael", "Joe", "Martin", "Watson"]
print(f"There are {len(players)} players in the team: ")
gamers = [print(player) for player in players]


# how to identify the number of items in a list?
print("\nlen - the number of items in a list")
nice_list = ["1", "2", "3", "4", "5", "6", "7", "8"]
print(len(nice_list))


"""
"""
print("Getting squares")
numbers = list(range(11))
for i in numbers: 
    square = i ** 2
    print(f"Square of {i} is {square}")

#same could be done with the following syntax: 
print("\nGetting squares with a different syntax")
people = [print(f"Square of {person} is {person**2}") for person in range(11)]


print("\nmillions")
million = range(1_000_000)
print(min(million), max(million))
print(sum(million))
print(million)
"""
""" 
print("Range from 1 to 5, the last variable doesn't count")
for i in range(1,6): 
    print(i)
    
print("Making list of some range")
special_list = list(range(1,6))
print(special_list)

print("Indicating only even or odd numbers")
print("list(range(A,B,C): A - begin; B - end excluded; C - step")
even_numbers = list(range(2,11,2))
odd_numbers = list(range(1,11,2))
print(f"Even: {even_numbers} & \nOdd: {odd_numbers}")

"""

#%%05.09.2022 
"""

# playing with lists.
friends = ["Iliyas", "Kirill", "Sultan", "Nurzhan"]
print(friends[0])
print(f"Hello, dear friends: {friends[0]}, {friends[1]}, {friends[2]}, {friends[3]}")

    
print("\nAppending new elements:")
some_list = ["item1", "item2", "item3"]
some_list.append("item4")
print(some_list)

# damn, that's quite interesting!
# some_list = some_list.append("item4") doesn't work!
# while simply some_list.append("item4") works... 

# working with changing the items on the list
print("\n")
some_list[0] = "ITEMA"
print(some_list)


# inserting elements: basically like list[item_count] = new_item_name
print("\nInserting new elements:")
some_list.insert(3, "item3_new")
print(some_list)
# now it adds for the third place: item3_new
some_list[0], some_list[-2], some_list[-1] = "item1", "item4", "item5" 
for i in some_list: 
    print(i)


# popping is opposite to appending. 
print(f"\nOld List: {some_list}")
some_list.pop()
print(f"Updated List with Pop: {some_list}")

#not only popping taking the value from the list but also can assign. 
print(f"Current list: {some_list}")
emitted_value = some_list.pop(-1)
print(f"Updated List without the last item: {some_list}")
print(f"Emitted value: {emitted_value}")


# removing items only with certain value name
print(f"Our current list: {some_list}")
removed_item = some_list.remove("item1")
print(f"Updated list without the removed item {removed_item}")
print(f"\nRemaining items on the list: {some_list}")

# sorting lists
int_list = [3, 5, 2, 4, 1]
int_list.sort()
print(int_list)

# sorting temporarily 


"""

#%% 

"""
print("Languages: \n\tPython, \n\tC++, \n\tJS")

text = "people "
print(text)
text = text.rstrip()
print(text)
"""

#%%
# some last code
"""
a = "hello, world!"
print(a.title())
print(a.upper())
print(a.lower())

first_name="alisher"
last_name="temirlanov"
full_name=f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}")
"""

