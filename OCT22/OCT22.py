#Created on Sat Oct  1 14:52:55 2022


#%% 19.10.2022. 

import time

count = 0

while True: 
    a = time.localtime()
    
    day, month, year, hour, minutes, sec = \
                a.tm_mday, a.tm_mon, a.tm_year, a.tm_hour, a.tm_min, a.tm_sec
    
    day, month, year, hour, minutes, sec = \
        str(day), str(month), str(year), str(hour), str(minutes), str(sec)
    
    
    the_time = f"Today is {day}.{month}.year, {hour}:{minutes}:{sec}"
    print(the_time)
    
    time.sleep(1)
    
    count +=1
    
    if count == 10: 
        break
    

    


# age = int(input("Tell us your age: "))
# if age < 3: 
#     print("Scenic River Cruise")
# elif age < 6: 
#     print("Carnival Carousel")
# elif age < 12: 
#     print("Jungle Adventure Water Splash")
# elif age < 70: 
#     print("The Regurgitator (a super scary roller coaster)")
# %% 18.10.2022. 
# numbers = int(input())
# arr = []
# for i in range(numbers): 
#     new_number = int(input())
#     arr.append(new_number)

# while True: 
#     times = 0 
#     zeros = arr.count(0)
    
#     if zeros == len(arr) - 1: 
#         print("NO")
#         break
#     elif sum(arr) == 0: 
#         print("YES")
#         break
    
#     for i in range(len(arr)): 
#         if arr[i] == 0: 
#             continue
#         arr[i] -= 1
#         times += 1
#         if times == 2: 
#             break


# inputs = int(input())
# while inputs: 
#     a = int(input())
#     b = int(input())
#     times = 0
#     while a % b != 0:
#         a += 1
#         times += 1
        
#     print(times)
#     inputs -= 1



# C1 = 100
# C2 = 50
# C3 = 20
# C4 = 10
# C5 = 5
# C6 = 2
# C7 = 1


# c1 = int(input())
# c2 = int(input())
# c3 = int(input())
# c4 = int(input())
# c5 = int(input())
# c6 = int(input())
# c7 = int(input())

# clients = int(input())

# summa = [c1*C1, c2*C2, c3*C3, c4*C4, c5*C5, c6*C6, c7*C7]
# total = sum(summa)

# while clients>0: 
#     amount = int(input())
#     if total >= amount: 
#         print("Transaction accepted!")
#     else:
#         print("Transaction stopped!")
        
#     total -= amount
#     clients -= 1



# times = int(input())
# while times>=0: 
#     a = int(input()) # dog food
#     b = int(input()) # cat food
#     c = int(input()) # universal food
#     x = int(input()) # dogs
#     y = int(input()) # cats
    
#     dogs = a-x
#     cats = b-y
#     if dogs >= 0: 
#         cats += c
#         if cats < 0: 
#             print("NO")
#         else: 
#             print("YES")
#     else: 
#         if c+dogs < 0: 
#             print("NO")
#         else: 
#             cats = cats + c - dogs 
#             if cats < 0: 
#                 print("NO")
#             else: 
#                 print("YES")
      
#     times =- 1

# class SomeClass: 
#     attr1 = "this is a class"
    
#     def fun1(self): 
#         return "This is a function"

# print(SomeClass.attr1)
# print(SomeClass.fun1(SomeClass))
# import time
# print("I will need to think about that...")
# time.sleep(3)
# print("The answer is 42")
#%% 17.10.2022. 

# from decimal import Decimal

# num1 = Decimal("19.15263748")
# print(num1.quantize(Decimal("0.00")))

# working with fractions

# imagine 2 and 1/2 = 2.5, right?
# now let's multiply it by 5/8

# import fractions

# num1 = fractions.Fraction(2.5)
# num2 = fractions.Fraction(5/8)
# prod = num1 * num2
# print(prod)

# from fractions import Fraction
# num1 = Fraction(2.5)
# num2 = Fraction(5/8)
# prod = num1 * num2
# print(prod)
# print(Fraction(24, 16)) # gives 3/2 

# import decimal

# the_number = decimal.Decimal("3.1264456789999") # making from int/float the decimal
# rounding = decimal.Decimal("0.00") # getting the rounding stuff for quantize()
# the_number = the_number.quantize(rounding, decimal.ROUND_DOWN) # voala!
# print(the_number)

# import decimal

# # here is the problem

# x = 1.0
# y = 1.0
# z = 1.0
# print(x+y+z/3) # gives 2.3333...5 instead of 1.0 - which is broken

# # here is what we need 
# x = "1.0" # note that it is not integer value but string!
# y = "1.0"
# z = "1.0"
# x, y, z = decimal.Decimal(x), decimal.Decimal(y), decimal.Decimal(z)
# print(x+y+z)

# # here is how we can round numbers

# num = 3.1415123123123
# num = str(num)
# num = decimal.Decimal(num)
# num = num.quantize(decimal.Decimal("0.00")) # keep in mind that it works because Decimal.quantize()
# print(num)

# from decimal import Decimal

# # some more example
# tax_rate = Decimal('7.25')/Decimal("100")
# purchase_amount = Decimal("2.95")
# total_amount = purchase_amount*(1+tax_rate)
# penny = Decimal("0.01")
# total_amount = total_amount.quantize(penny)
# print(total_amount)

#%% 15.10.2022. 

# # guessing game

# from random import randint
# cpu_number = randint(0,100)
# guesses = 0
# while True: 
#     try: 
#         number = int(input("Guess the number, please: "))
#     except ValueError: 
#         print("Only numbers, please!")
#         continue
#     if number == cpu_number: 
#         print(f"Great, you guessed it!\nIt took you {guesses} guesses!")
#         break
#     elif number > cpu_number: 
#         print("Your number is too high.")
#     elif number < cpu_number: 
#         print("Your number is too low.")
#     guesses+=1

# from string import punctuation

# text = "Hey, fuck! what a hell! you shit! stupid!"
# the_details = text.split()
# inappropriate_words = ["shit", "stupid", "fuck", "damn"]
# print(the_details)
# for i in the_details:
#     print(i.strip(punctuation))
#     if i.strip(punctuation) in inappropriate_words: 
#         print(i)
#         the_details.remove(i)

# L, M, S

# sizes = {}

# def transfer(size): 
#     sizes = []
#     if size[-1].upper() == "L": 
#         sizes[size] = 3
#     elif size[-1].upper() == "M": 
#         sizes[size] = 2
#     elif size[-1].upper() == "S": 
#         sizes[size] = 1
#     return 


# def sizeX(size): 
#     output = size
#     for i in range(len(str(size))-1): 
#         output *= 10
#     return output


# def compare(sizeA, sizeB): 
#     if sizeA > sizeB: 
#         print(f"{size1} > {size2}")
#     elif sizeA < sizeB: 
#         print(f"{size1} < {size2}")
#     else:
#         print(f"{size1} = {size2}")


# size1 = input("Give us the first size: ")
# size2 = input("Give us the second size: ")

# sizeA, sizeB = sizeX(transfer(size1)), sizeX(transfer(size2))
# compare(sizeA, sizeB)



#%% 14.10.2022. 
# # doing the factorial stuff
# import math

# def fact(number): 
#     output = 1
#     for i in range(1,number+1): 
#         output *= i
#     return output

# print(fact(500)==math.factorial(500))
# print(2**2048)        
# =============================================================================
# print("""Bagels, a deductive logic game. 
#       I am thinking of a 3-digit number. Try to guess what it is. 
#       Here are some clues: 
#       When I say:   That means: 
#         Pico      One digit is correct but in the wrong position. 
#         Fermi     One digit is corret and in the right position. 
#         Bagels    No digit is correct. 
#      
#         I have thought up a number. 
#           You have 10 guesses.
#       """)
# 
# from random import randint
# answer = str(randint(1,999))
# if len(answer) == 2:
#     answer = "0" + answer
# elif len(answer) == 1: 
#     answer = "00" + answer
# 
# answer = "123"
#     
# num1, num2, num3 = answer[0], answer[1], answer[2]
# answers = [num1, num2, num3]
# 
# guesses = 1
# while guesses <= 10: 
#     print(f"Guess #{guesses}")
#     while True: 
#         try: 
#             number = input("Give us a positive 3-digits number: ")
#             for i in number: 
#                 int(i)
#             number  = str(number)
#             if len(number) < 3 or len(number) > 3: 
#                 print("Only 3-digits numbers, please!")
#                 continue
#             break
#         except ValueError: 
#             print("Please, only numbers and positive ones!")
#             continue
#     
#     numbers = [number[0], number[1], number[2]]
#     
#     count = 0
#     
#     for i in numbers: 
#         if i in answers: 
#             if i == answers[number.index(i)]: 
#                 print("Fermi")
#             else: 
#                 print("Pico")
#         else: 
#             count +=1
#         if count == 3: 
#             print("Bagels")
# 
#     if numbers == answers: 
#         print("You got it!")
#         break
# 
#     guesses += 1
# 
# print("Great job!")
# =============================================================================
# text = "Hello, World!"
# print(text.lower())
# number = "10"
# number = str.lower(number)
# print(number)

# user_input = input("Give us a word: ")
# user_input = list(user_input)
# vowels = ["a", "o", "e", "u", "i"]
# if user_input[0] in vowels: 
#     user_input.append("way")
#     user_input = "".join(user_input)
# else: 
#     item = user_input.pop(0)
#     user_input = "".join(user_input)
#     user_input = user_input + item + "ay"
# print(user_input)

# list1 = [1,2,3,4,5]
# list2 = ["one", "two", "three", "four", "five"]
# list3 = ["P1", "P2", "P3", "P4", "P5"]

# for item1, item2, item3 in zip(list1, list2, list3): 
#     print(item1, item2, item3)
# # cool stuff! 
# info1 = ["Alisher", "Kirill", "Iliyas"]
# info2 = [24, 25, 24]
# info3 = ["Python Dev", "JS Dev", "PM"]
# info4 = [True, False, True]
# full_info = list(zip(info1, info2, info3, info4))
# print(full_info)
#%% 13.10.2022. 
# nocode day... too bad :\
#%% 12.10.2022. 
# =============================================================================
# # feet and inches (1 foot = 12 inches; 1 inch = 2.54cm)
# user_feet = int(input("How many feet do you have? "))
# user_inches = int(input("How many inches do you have? "))
# user_height_cm = (user_feet * 12 + user_inches) * 2.54
# print(f"Your height is {user_height_cm} centimeters")
# =============================================================================
# =============================================================================
# # change giver with coins
# # my solution!:)
# # 100 pennies, 20 nickels, 10 dimes, 4 quarters, 1 loonie, and 0.5 toonie in 1$
# 
# from math import floor
# 
# coins = {"toonies": 0, "loonies": 0.0, "quarters": 0.0, "dimes": 0.0, 
#          "nickels": 0.0, "pennies": 0.0}
# 
# cash = float(input("How much change we should give you back? "))
# 
# whole = floor(cash)
# if whole % 2 == 0: 
#     coins["toonies"] = whole/2
# else: 
#     coins["toonies"] = (whole-1)/2
#     coins["loonies"] = 1.0
# 
# if cash >= 1: 
#     decimals = (cash % whole)*100
# else: 
#     decimals = cash*100
# 
# while True: 
#     if decimals // 25 >= 1: 
#         coins["quarters"] = quarters = decimals//25
#     else: 
#         quarters = 0
#     if (decimals-quarters*25) // 10 >= 1: 
#         coins["dimes"] = dimes = (decimals-quarters*25)//10
#     else: 
#         dimes = 0
#     if (decimals-quarters*25-dimes*10) // 5 >= 1:
#         coins["nickels"] = nickels = (decimals-quarters*25-dimes*10)//5
#     else: 
#         nickels = 0
#     if (decimals-quarters*25-dimes*10-nickels*5) // 1 >= 1:
#         coins["pennies"] = pennies = (decimals-quarters*25-dimes*10-nickels*5)//1
#     else: 
#         pennies = 0.0
#     break
# 
# for keys, values in coins.items(): 
#     print(f"There are {int(values)} {keys} in {cash}")
# 
# print(quarters, dimes, nickels, pennies)
# =============================================================================
# =============================================================================
# # the solution of the author - a bit different approach but still fine
# coins = {"toonies": 0, "loonies": 0, "quarters": 0, "dimes": 0, "nickels":0, 
#          "pennies":0}
# 
# cash = int(input("How much change do you need? "))
# 
# coins["toonies"] = cash // 200
# left = cash % 200
# coins["loonies"] = left // 100
# left = cash % 100
# coins["quarters"] = left // 25
# left = cash % 25
# coins["dimes"] = left // 10
# left = cash % 10
# coins["nickels"] = left // 5
# left = cash % 5
# coins["pennies"] = left // 1
# 
# for keys, values in coins.items(): 
#     print(f"There are {int(values)} {keys} in {cash}")
# =============================================================================
# =============================================================================
# import math 
# t1 = math.radians(43.23)
# g1 = math.radians(76.91)
# t2 = math.radians(51.51)
# g2 = math.radians(-0.09)
# distance = 6371.01 * math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
# print(distance)
# 
# t1 = math.radians(43.23)
# g1 = math.radians(76.91)
# t2 = math.radians(40.71)
# g2 = math.radians(-74.01)
# distance = 6371.01 * math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
# print(distance)
# 
# t1 = math.radians(43.23)
# g1 = math.radians(76.91)
# t2 = math.radians(50.42)
# g2 = math.radians(80.25)
# distance = 6371.01 * math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
# print(distance)
# =============================================================================
#%% 11.10.2022. 
# =============================================================================
# list100 = list(range(1,101))
# result = sum(list100)/len(list100)
# print(result)
# =============================================================================
# =============================================================================
# # practicing again with else statements for "for":D
# # the most important thing is the break that stops for and while to go into else
# places = ["France", "UK", "US", "Italy", "China"]
# theplace = "China"
# for place in places: 
#     if theplace == place: 
#         print(f"The place {theplace} is in places!")
#         break
#     else: 
#         print(place)
#     if place == "Italy": #so it doesn't even reach China and doesn't reach else
#         break
# else: 
#     print("There is no such a place in places:",theplace)
#     
# # with while
# print("\nWith while: ")
# while places: 
#     if places[0] == "China": 
#         print(f"The place {theplace} is in places!")
#         #It doesn't stop here because we didn't indicate break!
#     places.pop(0)
# else: 
#     print("There is no such a place in places:",theplace)
# 
# # with break
# places = ["France", "UK", "US", "Italy", "China"]
# print("\nWith while: ")
# while places: 
#     if places[0] == "China": 
#         print(f"The place {theplace} is in places!")
#         break
#         #It doesn't stop here because we didn't indicate break!
#     places.pop(0)
# else: 
#     print("There is no such a place in places:",theplace)
# =============================================================================
# =============================================================================
# people = ["Jack", "Jucy", "Jane", "John", "Jack", "Jucy", "Jane"]
# count = 0
# count1 = 0
# for i in people: 
#     if i.startswith("J"):
#         count +=1
#     if i[0] == "J": 
#         count1+=1
#         
# print(count,count1)
# =============================================================================
# =============================================================================
# # tribonacci let's go!
# tribonacci = [1,1,2]
# while True: 
#     try: 
#         number = int(input("Give us a number: "))
#         if number <= 3 and number > 0: 
#             print(f"Your number is {tribonacci[number-1]} in Tribonacci")
#             break
#         elif number <= 0:
#             print("Only positive numbers, please!")
#             continue
#         elif number >3: 
#             for i in range(3,number): 
#                 tribonacci.append(i)
#                 tribonacci[-1] = tribonacci[-2] + tribonacci[-3] + tribonacci[-4]
#             print(f"Your number is {tribonacci[number-1]} in Tribonacci")
#             break
#     except ValueError: 
#         print("Only numbers, please!")
# 
# print(tribonacci)
# =============================================================================
# =============================================================================
# # copying elements from 1 object to another one via 3 different ways
# lista = [1,2,3]
# listb = lista
# listc = lista.copy()
# listd = lista[:]
# liste = list(lista)
# lists = [lista, listb, listc, listd, liste]
# print("(1.0) Our Lists: ")
# for i in lists: 
#     print(i)
# 
# lista.append(4)
# print("\n(1.1) Updated Lits: ")
# for i in lists: 
#     print(i)
# 
# lista[-2] = "three"
# print("\n(1.2) Updated Lits: ")
# for i in lists: 
#     print(i)
# # so no changes to the copied lists
# # how about the modifiable items like lists themselves?
# lista = [1,2,3,[4,5,6]]
# listb = lista
# listc = lista.copy()
# listd = lista[:]
# liste = list(lista)
# lists = [lista,listb,listc,listd,liste]
# print("\n(2.0) Our New Original Lists: ")
# for i in lists: 
#     print(i)
# 
# lista[-1][0] = "four"
# print("\n(2.1) Updated Lits: ")
# for i in lists: 
#     print(i)
# 
# # here we go! everything has changed!
# # to prevent that we need deepcopy from module copy
# import copy
# 
# lista = [1,2,3,[4,5,6]]
# listb = copy.deepcopy(lista)
# lists = [lista,listb]
# print("\n(3.0) Our New Original Lists: ")
# for i in lists: 
#     print(i)
# 
# lista[-1][-1] = "six"
# print("\n(3.1) Updated Lits: ")
# for i in lists: 
#     print(i)
# #alright, here we go.
# =============================================================================
# =============================================================================
# import string
# # splitting and joining!
# # first splitting
# print("First splitting: ")
# some_text = "Hello, dear friends! How are you doing? We are so glad to see you!"
# some_text = some_text.split()
# new_text = []
# for i in some_text: 
#     new_text.append(i.strip(string.punctuation))
# 
# print(new_text)
# 
# print("\nNow joining: \n")
# # now joining
# print(f"Original list with items: {some_text}")
# print("\nTransformed into text: ")
# some_text = " ".join(some_text)
# print(some_text)
# =============================================================================
#%% 10.10.2022. 
# =============================================================================
# some_array = "hey john what is up!".split()
# print(some_array)
# print(some_array.index("up!"))
# 
# people = ["Jack", "Jucy", "Jane", "John", "Jack", "Jucy", "Jane"]
# print(people.count("Jack"))
# 
# print("Jordan" in people)
# print("Jack" in people)
# =============================================================================
# =============================================================================
# # removing items with various ways
# elements = [False, 1,"2", "three", "'4'", "V",["111111"], {"elements": 7}]
# print(f"The initial list of elements: \n{elements}")
# popped = elements.pop() # pop is about the last element or any indicated
# popped_2 = elements.pop(5)
# print("\nUpdated list: ")
# print(elements)
# print("\nPopped items: ")
# print(popped)
# print(popped_2)
# 
# for i in ["three", False]: 
#     elements.remove(i) # removing items by naming them
# print("\nUpdated elements without removed items: ")
# print(elements) 
# 
# del elements[-1] # indicating the index
# print("\nUpdated elements without elements[-1]: ")
# print(elements)
# =============================================================================
# =============================================================================
# # another nice example of slicing
# our_numbers = [i for i in range(0,11)]
# print(our_numbers)
# our_numbers[3:6] = our_numbers[5:2:-1]
# print(our_numbers)
# our_numbers[-3:] = 10,9,8 # or [10,9,8] - same effect
# print(our_numbers)
# =============================================================================
# =============================================================================
# original_list = [1]
# new_list = original_list * 3
# third_list = [i * 3 for i in new_list]
# 
# print(original_list) # seeing original list
# original_list.extend(third_list) # we are adding third list to the original one
# print(original_list) # seeing the modified list
# 
# print(third_list) # original third list
# third_list += new_list # adding with '+' the new list
# print(third_list) # seeing the change
# =============================================================================
# =============================================================================
# numbers = [i for i in range(0,11)]
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)
# print()
# names = ["John", "Michael", "Drake", "Chris", "Mark", "Frank"]
# print(names)
# names.reverse()
# print(names)
# print()
# print(sorted(names)) # it is like .sort() but doesn't change the list
# print(names)
# names.sort()
# print(names)
# =============================================================================
# =============================================================================
# # going through the list with slicing
# some_list = [1,2,3,4,5,6,7,8,9,10]
# print(some_list[:]) # pringing all the elemenets
# print(some_list[3:-3]) # printing from the fourth til the 3 from the end
# print(some_list[-3:]) # from third from the end until the end
# print(some_list[1::2]) # will print every second item from the second one
# print(some_list[-1:0:-1]) # from end til the beginning except the first one!
# print(some_list[-1::-1]) # from end til the very beginning - logical!
# =============================================================================
# =============================================================================
# # here's how we can add to tuples
# some_tuple = (1, False)
# print(some_tuple)
# some_tuple += (1,) 
# print(some_tuple)
# print(type(some_tuple[-1]))
# =============================================================================
# =============================================================================
# # we were told that lists and tuples can contain any data types. Let's check it
# #0) basics are clear: string, int/float, other lists, dicts etc.
# # how about functions and classes?
# def fun(): 
#     pass
# 
# class Class: 
#     def __init__(self, number): 
#         self.number = number
#         print(self.number)
# 
# some_list = [0, fun, Class(10)]
# for i in some_list: 
#     print(type(i))
# =============================================================================
# =============================================================================
# guess_me = 7
# number = 1
# while True: 
#     if number < guess_me: 
#         print("Too low!")
#     elif number == guess_me: 
#         print("Found it!")
#     else: 
#         print("Ooops!")
#         break
#     number+=1
# =============================================================================
# =============================================================================
# guess_me = 7
# number = 1
# while number < guess_me: 
#     print("Too low")
#     number +=1
# else: 
#     print("Found it!")
# =============================================================================
# =============================================================================
# some_list = [i for i in range(10,-1,-1)]
# print(some_list)
# =============================================================================
# =============================================================================
# # something we opened earlier this month - range can run backwards
# for i in range(10,-1,-1): 
#     print(i)
# =============================================================================
# =============================================================================
# guests = ["Michael", "Joseph", "Jackson"]
# name = "John"
# for guest in guests: 
#     if guest == name: 
#         print(f"{name} is in guests!")
#         break
# else: 
#     print(f"{name} is NOT in guests!")
# =============================================================================
# =============================================================================
# numbers = [1,3,5]
# position = 0
# while position < len(numbers): 
#     number = numbers[position]
#     if number % 2 == 0: 
#         print("We've found an even number!", number)
#         break
#     position +=1
# else:
#     print("No even number found!")
#     
# # quite strange stuff with else above. Let's check 1 more
# 
# flag = True
# while flag: 
#     if flag is False: 
#         print("Flag is False!")
#     flag = False
# 
# else: 
#     print("Flag is actually True!")
#     
# # I just got it. Else is used not only with if but also with while! Damn...
# =============================================================================
#%% 09.10.2022. 

# """class Client:
#     def __init__(self, name):
#         print(f"Client: {name}")
#         self._name = name
# 
#     def get_connection_name(self):
#         return self._name
# 
#     def after_close(self):
#         print("Client: close")
# 
# 
# class ClientForWith:
#     def __init__(self, name):
#         self._client = Client(name)
# 
#     def __enter__(self):
#         return self._client
# 
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self._client.after_close()
# 
# 
# client = Client("John")
# print(client.get_connection_name())
# 
# with ClientForWith("Amadeus") as conn:
#     conn.get_connection_name()
# """
# """
# with open("hello_world.txt", "w") as file:
#     file.write("Hello, World!")
# """
# 
# """
# class User:
#     def __init__(self, login, password):
#         self.login = login
#         self.password = password
# 
# 
# class AuthClient:
#     user = None
# 
#     def __init__(self, login, password):
#         self.user = User(login, password)
# 
#     def __enter__(self):
#         print(f'User {self.user.login} is online')
#         return self
# 
#     def send_message(self):
#         print(f"Hello, dear {self.user.login}!")
# 
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(f"User {self.user.login} is offline")
# 
# 
# with AuthClient("alitim179", "12345TAT") as session:
#     session.send_message()
#     exit()
# """
# 
# 
# """
# from contextlib import contextmanager
# 
# 
# class UserAuth:
#     def __init__(self, acc, passw):
#         self.acc = acc
#         self.passw = passw
# 
#     def info(self):
#         print(f"The user's login is {self.acc} and password is {self.passw}")
# 
#     def __enter__(self):
#         print("The session has started")
#         return self
# 
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("The session has expired.")
# 
# 
# with UserAuth("alitim179", "12345TAT") as session:
#     session.info()
#     exit()
# 
# 
# # subscribe to the channel
# # yield - listing all users who subscribed
# 
# """
# """
# # decorators
# def my_decorator(func):
#     def wrapper(): # the function which takes over the main function and does something with it;
#         print("Entrance")
#         func()
#         print("Exit")
# 
#     return wrapper
# 
# @my_decorator
# def my_func():
#     print("Hello!")
# 
# my_func()
# """
# 
# """
# import requests
# 
# 
# def my_decorator(func):
#     def wrapper():
#         import time
#         start = time.time()
#         func()
#         end = time.time()
#         print(end-start)
# 
#     return wrapper
# 
# @my_decorator
# def my_func():
#     print("Hello!")
#     import requests
#     res = requests.get("https://book.pythontips.com/en/latest/decorators.html")
# 
# 
# my_func()
# """
 
# def main_decorator(n):
#     def my_decorator(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
# 
#             return result ** n
# 
#         return wrapper
# 
#     return my_decorator
# 
# 
# @main_decorator(4)
# def my_func():
#     return 5
# 
# 
# print(my_func())


# =============================================================================
# #guessing game from 1 to 100
# from random import randint
# 
# print("Let's play the guessing game!")
# print("Try to guess the number from 1 to 100!")
# number = randint(1, 100)
# count = 0
# while True: 
#     try: 
#         usrn = int(input("Give us a number: "))
#         if usrn <= 0: 
#             print("Only positive numbers, please!")
#             continue
#     except ValueError: 
#         print("Only numbers, please!")
#         continue
#     if usrn == number: 
#         print(f"You guessed it right! The number is {number}")
#         break
#     elif usrn < number: 
#         print("The number is lower than needed, score higher!")
#     else: 
#         print("The number is higher than needed, score lower!")
#     
#     count +=1
# 
# print(f"Great! It took you just {count} times to guess it right!")
# 
# =============================================================================
# =============================================================================
# # alright, let's work out with function inside a function
# def usr_name():
#     name = input("What is your name? ")
#     return name
# 
# 
# def usr_surname():
#     surname = input("What is your surname? ")
#     return surname
# 
# 
# def usr_info(name, surname):
#     info = f"User's full name is {name} {surname}."
#     return info
# 
# 
# # print(usr_info(surname=usr_surname(), name=usr_name()))
# 
# 
# # now let's try out the damn decorators
# 
# def usr_name(name):
#     return f"User's name is {name}"
# 
# 
# def usr_surname(surname):
#     return f"User's surname is {surname}"
# 
# 
# def usr_info(usr_name, usr_surname):
#     def info():
#         print("User's full info is as following: ")
#         print(usr_name())
#         print(usr_surname())
# 
#     return info
# 
# =============================================================================
# =============================================================================
# def person_info(individual): 
#     def greeting(): 
#         print("Hello, dear person!")
#         individual()
#     return greeting
# 
# @person_info
# def individual(name):
#     print(f"You are a great person, mister {name}") 
# 
# individual("Alisher")
# 
# 
#     
# =============================================================================


#%% 08.10.2022.
# =============================================================================
# """
# class Car:
#     def __init__(self, name):
#         self.name = name
#         self.year = 1999
#         self.car_kind = "Blue"
#         self.car_color = " "
# 
#     def car_launch(self):
#         print(f"The {self.name} is launched.")
# 
#     def car_exit(self):
#         print(f"The {self.name} is turned down.")
# 
#     def car_year(self):
#         self.year = int(input("What year is the car? "))
# 
#     def car_type(self):
#         self.car_kind = input("What type is the car? ")
# 
#     def color(self):
#         self.car_color = input("What color is the car? ")
# 
# 
# mycar = Car("Tesla")
# mycar.car_launch()
# mycar.car_year()
# mycar.car_exit()
# mycar.color()
# mycar.car_type()
# """
# 
# """
# class HouseA:
#     pass
# 
# def declaration(self):
#     print("This is a great house!")
# 
# HouseA.new_method = declaration
# myhouse = HouseA()
# myhouse.new_method()
# """
# """
# class Triangle:
#     def __init__(self):
#         self.sideA = None
#         self.sideB = None
#         self.sideC = None
# 
#     def A(self):
#         self.sideA = int(input("What is the size of side A: "))
# 
#     def B(self):
#         self.sideB = int(input("What is the size of side B: "))
# 
#     def C(self):
#         self.sideC = int(input("What is the size of side C: "))
# 
#     def is_triangle(self):
#         is_triangle = True
#         sides = [self.sideA, self.sideB, self.sideC]
#         for side in sides:
#             if side > sum(sides) - side:
#                 is_triangle = False
#     
#         return is_triangle
# 
# 
# triangle = Triangle()
# triangle.A()
# triangle.B()
# triangle.C()
# 
# if triangle.is_triangle():
#     print("This is a triangle")
# else:
#     print("This is NOT a triangle")
# """
# """
# class A:
#     def __init__(self):
#         self._attr = 2
# 
#     def my_method(self):
#         print(self._attr)
# 
# 
# my_class = A()
# my_class.my_method()
# print(my_class._attr)
# """
# """
# class Name:
#     name = None
# 
#     def my_name(self):
#         self.name = input("What is your name: ")
# 
# 
# class Surname:
#     surname = None
# 
#     def my_surname(self):
#         self.surname = input("What is your surname: ")
# 
# class Info(Name, Surname):
#     def info(self):
#         print(f"Hello! My name is {self.name} {self.surname}")
# 
# 
# person = Info()
# person.my_name()
# person.my_surname()
# person.info()
# """
# """
# class Group:
# 
#     def __init__(self, name):
#         self.name = name
# 
# 
# class Student:
# 
#     def __init__(self, name, group):
#         self.name = name
#         self.group = group
# 
#     def __str__(self):
#         return f'student: {self.name} | group: {self.group.name}'
# 
# 
# csse1603 = Group('CSSE-1603')
# csse1605 = Group('CSSE-1605')
# 
# aibar = Student('Aibar', csse1603)
# madina = Student('Madina', csse1603)
# alisher = Student('Alisher', csse1605)
# aizhan = Student('Aizhan', csse1605)
# daniyar = Student('Daniyar', csse1605)
# 
# print(aibar)
# print(alisher)
# """
# """
# class Info:
#     pass
# 
# 
# class Game(Info):
#     def __init__(self):
#         self.name = "Game's name"
# 
#     def info(self):
#         return f"The game's name is {self.name}"
# 
# 
# game = Game().name
# print(game)
# 
# 
# def change_data(self):
#     print("We appoint the New Name")
#     self.name = input("What is the updated name? ")
# 
# 
# Game.change_data = change_data
# new_game = Game()
# print(new_game.info())
# new_game.change_data()
# print(new_game.info())
# """
# """
# class Country: 
#     
#     def __init__(self, name): 
#         self.name = name
#         self.foundation = None
#         self.citizens = None
#     
#     def Name(self): 
#         self.name = input("The name of the country: ")
#         
#     def Foundation(self): 
#         self.foundation = int(input("Year of foundation: "))
#     
#     def Citizens(self): 
#         self.citizens = int(input("What is the population of the country: "))
#     
#     def Info(self): 
#         print(f"{self.name} was founded in {self.foundation} with "
#               f"current population of {self.citizens} people.")
#     
# KZ = Country("Republic of Kazakhstan")
# KZ.Foundation()
# KZ.Citizens()
# KZ.Info()
# """        
# =============================================================================
#%% 07.10.2022.
# =============================================================================
# """
# deposit = int(input("How much money would you like to deposit: "))
# years = int(input("How many years would you like to save for: "))
# amounts = {}
# amount = deposit * 1.04
# for i in range(1,years+1): 
#     amounts[i] = round(amount,2)
#     amount = amount * 1.04
#     
# for info, data in amounts.items(): 
#     print(f"In the year {info} the amount is {data}")
# 
# """
# 
# """
# #widgets and gizmos 
# widget = 75
# gizmo = 112
# while True: 
#     try: 
#         numwidgets = int(input("What number of widgets: "))
#         if numwidgets <= 0: 
#             print("Only positive numbers, please!")
#             continue
#         numgizmos = int(input("What number of gizmos: "))
#         if numgizmos <= 0: 
#             print("Only positive numbers, please!")
#             continue        
#     except ValueError: 
#         print("Only numbers, please!")
#         continue
#     break
# total = widget * numwidgets + gizmo * numgizmos
# print(f"The total weight of the products is {total}")
# 
# """
# """
# while True: 
#     try: 
#         usrn = int(input("Give us a positive integer: "))
#         if usrn <=0: 
#             print("Only positive integers, please!")
#             continue
#     except ValueError: 
#         print("Only numbers, please!")
#         continue
#     break
# n = usrn
# summa1 = n*(n+1)//2
# print(summa1)
# summa2=0
# for i in range(1, n+1): 
#     summa2 += i
# print(summa2)
# 
# """
# 
# """
# #working on some orders
# print("Let's learn how much you need to pay for your meal!")
# orders = []
# num_orders = int(input("How many orders did you make? "))
# for i in range(1, num_orders+1): 
#     title = input(f"What is the title of the {i} order? ")
#     cost = float(input(f"How much did {title} cost you? "))
#     #counting the tax & tip & total
#     tax = cost*0.15
#     tip = cost*0.18
#     total = cost+tax+tip
#     #putting the info into dicts
#     new_order = {"title": title, "order": i, "cost": cost, "tax": tax, "tip": tip, "total": total}
#     orders.append(new_order)
# 
# for i in orders: 
#     print(f"""
# #The order's title is {i["title"]}
# #The order number is {i["order"]}
# #Costs {i["cost"]}
# #Plus tax {i["tax"]} and tip {i["tip"]}
# #Totalling into {i["total"]}
# """) 
# """
# 
# """
# #containers and volumes
# containers = int(input("How many containers do you have? "))
# conts = {}
# for i in range(1, containers+1): 
#     conts[i] = float(input(f"What volume is your container number {i}? "))
# 
# for cont, vol in conts.items(): 
#     if vol <=1: 
#         dep = "0.10$"
#     else: 
#         dep = "0.25$"
#     print(f"Container {cont} has {vol} volume and you will get {dep} deposit.")
# """
# """
# #some old school stuff
# name = "John"
# x = 100.10
# numCookies = 12
# print("%.2f" % x)
# print("%s %s ate %d cookies!" % (name, name, numCookies))
# """
# """
# #playing with index and find
# text = """
# #Created on Wed Oct  5 12:52:21 2022
# #@author: alitim179
# """
# print(text.find("a"))
# print(text.index("a"))
# try:     
#     print(text.find("z"))
#     print(text.index("z"))
# except ValueError: 
#     print("The string is not found!:)")
# """
# """
# # working with strip
# print("Some string: ")
# some_string = "    Hey, guys, sup!    "
# print(some_string)
# print(some_string.strip())
# print(some_string.rstrip())
# print(some_string.lstrip())
# 
# print("\nAnother string: ")
# another_string = "Yaaaay!!!???..."
# print(another_string)
# print(another_string.strip("!.?"))
# 
# import string
# print("\nLast string: ")
# last_string = "!@#$%^&*(? Heellllll!!!!@#$%^&*(??"
# print(last_string)
# print(last_string.strip(string.punctuation))
# print("To remove the whitespace at the beginning we add "
#       "it to the strip along with punctuation: ")
# print(last_string.strip(f"{string.punctuation} "))
# """
# """
# #working with split and join
# some_str = "Hello, World! It is such a bless to see you!!!"
# some_str = some_str.split()
# print(some_str)
# some_str = " ".join(some_str)
# print(some_str)
# """
# """
# #nice example of ranging backwards:
# some_list = []
# for i in range(21,11,-4): 
#     some_list.append(i)
# print(some_list)
# """
# =============================================================================
#%% 05.10.2022.
# =============================================================================
# """
# import heapq
# nums = [1,4,7,11,14,8,9,0,10,12]
# print(heapq.nlargest(4, nums))
# print(heapq.nsmallest(4, nums))
# 
# portfolio = [
#     {"name": "IBM", "shares": 100, "price": 91.1}, 
#     {"name": "AAPL", "shares": 50, "price": 543.22}, 
#     {"name": "FB", "shares": 200, "price": 21.09}, 
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
#     ]
# 
# cheap = heapq.nsmallest(3, portfolio, key = lambda s: s["price"])
# expensive = heapq.nlargest(3, portfolio, key = lambda s: s["price"])
# print("")
# print(cheap)
# print("")
# print(expensive)
# """
# 
# """
# # playing with yield
# def some_fun():
#     yield "Hello!"
#     yield "What"
#     yield "is"
#     yield "your"
#     yield "name?"
# 
# for i in some_fun():
#     print(i)
# """
# """
# from collections import deque
# 
# def search(lines, pattern, history=5): 
#     previous_lines = deque(maxlen=history)
#     for line in lines: 
#         if pattern in line: 
#             yield line, previous_lines
#         previous_lines.append(line)
# 
# 
# if __name__ == "__main__": 
#     with open("somefile.txt") as f: 
#         for line, prevlines in search(f, "python", 5): 
#             for pline in prevlines: 
#                 print(pline, end="")
#             print(line, end="")
#             print("-"*20)
# 
# """
# """
# # fibonacci numbers again!!!
# # 0. basic algorithm 
# # we get a number as an index and give the nth number of the fibonacci series
# 
# user = int(input("Give us a number, please: "))
# 
# # creating the series
# 
# def fib(user): 
#     fib_series = [0,1]
#     for i in range(2, user+1):
#         fib_series.append(i)
#         fib_series[i] = fib_series[i-1] + fib_series[i-2]
#     
#     print(fib_series[user-1])
# 
# fib(user)
# # damn that seemed harder before!
# 
# """
# """
# # 1. with recursive function
# import sys
# 
# user = int(input("Give us a number: "))
# 
# def fibonacci(number, series = [0,1]): 
#     if number == 0:
#         print("The number is 0")
#     elif number == 1:
#         print("The number is 1")
#     elif number >= 2:
#         series.append(number)
#         series[-1] = series[-2] + series[-3]
#         if len(series) == number: 
#             print(f"Your number is {series[-1]}th")
#         else: 
#             fibonacci(number, series)
#     else: 
#         print("Pease, give only positive numbers next time!")
#         sys.exit()
# 
# fibonacci(user)
# """
# """
# # printing the following stuff
# #a
# #bc
# #def
# #ghij
# 
# alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
# alphabet = alphabet.split()
# print(alphabet)
# for i in range(9): 
#     temp = ""
#     for j in alphabet[:i]: 
#         temp += j
#         alphabet.remove(j)
#     
#     print(temp)
# 
# """
# """
# # prime numbers 
# # they divide to themselves and 1 only
# 
# user_input = int(input("Give us a number, please: "))
# 
# def prime_or_not(number):
#     a = None
#     for i in range(2, number): 
#         if number % i == 0: 
#             a = "prime"
#             print(f"{number} is not Prime")
#             break
#     
#     if a != "prime": 
#         print(f"{number} is Prime")
#     
# 
# prime_or_not(user_input)
# """
# """
# #0) Task: 
# 1=1
# 1+2=3
# 1+2+3=6 etc.
# 
# #1) simple algorithm
# 
# prompt = int(input("Give us a number: "))
# 
# some_list = []
# 
# for i in range(1,prompt+1): 
#     some_list.append(i)
# 
# temp = ""
# 
# for j in some_list: 
#     if j == some_list[-1]: 
#         temp += f"{j}"
#         print(f"{temp}={sum(some_list[:j])}")
#     elif j == some_list[0]: 
#         temp += f"{j}"
#         print(f"{temp}={temp}")
#         temp += "+"
#     else: 
#         temp += f"{j}"
#         print(f"{temp}={sum(some_list[:j])}")
#         temp += "+"
# 
# """
# """
# #2) work with the function
# 
# prompt = int(input("Give us a number: "))
# 
# some_list = []
# 
# for i in range(1,prompt+1): 
#     some_list.append(i)
# 
# def function(input_list): 
#     temp = ""
# 
#     for j in input_list: 
#         if j == input_list[-1]: 
#             temp += f"{j}"
#             print(f"{temp}={sum(some_list[:j])}")
#         elif j == input_list[0]: 
#             temp += f"{j}"
#             print(f"{temp}={temp}")
#             temp += "+"
#         else: 
#             temp += f"{j}"
#             print(f"{temp}={sum(some_list[:j])}")
#             temp += "+"
#     
# function(some_list)
# """
# """
# #3) another way
# 
# user_number = int(input("Give us a number: "))
# 
# def multy(entry_number): 
#     
#     temp = ""
#     temp_list = []
#     for i in range(1, entry_number+1): 
#         if i == 1: 
#             print(f"{i}={i}")
#             temp+=str(i)
#             temp_list.append(i)
#         else: 
#             temp_list.append(i)
#             print(f"{temp}+{i}={sum(temp_list)}")
#             temp+=f"+{str(i)}"
# 
# multy(user_number)
# """
# """
# # recursive function 
# user_number = int(input("Give us a number: "))
# def multy(entry_number, number=1, summa = [], temp=""): 
#     summa.append(number)
#     if number == 1: 
#         print(f"{number}={number}")
#         temp+= f"{number}"
#     else: 
#         print(f"{temp}+{number}={sum(summa)}")
#         temp+= f"+{number}"
#     
#     number+=1
#     
#     if number <= entry_number: 
#         return multy(entry_number, number, summa, temp)
# 
# multy(user_number)
# """
# =============================================================================

#%% 04.10.2022. 
# =============================================================================
# """
# # working with the star
# n = int(input("Give us a number: "))
# a = ""
# for i in range(1,n+1): 
#     a += "*"
#     print(a)
# length = len(a)
# for i in range(1, n+1): 
#     print(length * "*")
#     length -= 1
# 
# """"""
# some_list = [1,2,3,4,5,6,7,8,9,10]
# 
# def sum(items): 
#     head, *tail = items
#     return head + sum(tail) if tail else head
# 
# print(sum(some_list))
# 
# """
# """
# # bubble sort
# 
# some_list = [17, 3, 30, 41, 24, 35, 50, 12]
# for i in range(len(some_list)-1):
#     for j in range(len(some_list)-1): 
#         if some_list[j] > some_list[j+1]: 
#             temp = some_list[j]
#             some_list[j] = some_list[j+1]
#             some_list[j+1] = temp
#             
#             # same as: 
#             # some_list[j], some_list[j+1] = some_list[j+1], some_list[j]
# 
# print(some_list)
# 
# """
# 
# 
# """
# # working with some recursion
# 
# def some_fun(num, limit): 
#     if num < limit: 
#         num += 1
#         return some_fun(num, limit)
# 
# some_fun(1,100)
# 
# """
# =============================================================================
#%% 03.10.2022.
# =============================================================================
# """
# some_text = "Many users_try to_apply great tools_in their daily lives"
# item1, *item2, item3 = some_text.split('_')
# print(item2)
# 
# cities = ["Astana", "Almaty", "Shymkent", "Taraz", "Taldykorgan", "Semey"]
# *capitals, _, _, _, _ = cities
# print(*capitals)
# 
# """
# 
# """
# line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
# uname, *fields, homedir, sh = line.split(":")
# items = [uname, fields, homedir, sh]
# for i in items: 
#     print(i)
# 
# print("")
# for i in fields: 
#     print(i)
# 
# """
# 
# """
# John_Davis = {
#     "name": "John", 
#     "surname": "Davis", 
#     "age": 24, 
#     "funny_fact": "Hero of my novel"}
# 
# def name_info(name): 
#     print(f"The hero's name is {name}")
# 
# name_info(John_Davis["name"])
# """
# """
# some_array = (1,True,"5")
# for i in some_array: 
#     print(i)
# """
# 
# """
# records = [
#     ("full_info", "Alisher", "24"),
#     ("some_info", "25"),
#     ("full_info", "John", "100+"), 
#     ("some_info", "100+")]
# 
# def full(a,b): 
#     print("Full Info: ", a,b)
# def some(a): 
#     print("Some Info: ", a)
# 
# for tag, *args in records: 
#     if tag == "full_info": 
#         full(*args)
#     if tag == "some_info": 
#         some(*args)
# 
# """
# 
# =============================================================================
#%% 02.10.2022. 
# =============================================================================
# """
# def get_fib(n, arr=(1, 1), current_ind=3):
#     if n in (1, 2):
#         return 1
# 
#     new_value = arr[-1] + arr[-2]
# 
#     if current_ind == n:
#         return new_value
# 
#     arr += (new_value,)
#     current_ind += 1
# 
#     return get_fib(n, arr, current_ind)
# 
# print(get_fib(10))
# """
# 
# """
# # 01.10.2022. 
# 
# # fibonnacci number
# fibonacci_nums = [1,1]
# 
# def fib_num(n):
#     nonlocal number1, number2
#     number1 = number2 = 1
#     if n < 3:
#         if n == 1:
#             n = number1
#         elif n == 2:
#             n = number2
#         else:
#             print("Only positive numbers, please!")
#     count = 0
#     while count < n:
#         nth = number1 + number2
#         number2 = nth + number1
#         number1 = nth + number2
#         count += 1
#     
#     return nth
# 
# print(fib_num(10))
# """
# =============================================================================