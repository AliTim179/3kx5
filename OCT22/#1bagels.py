#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 13:16:11 2022

@author: alitim179
"""

print("""Bagels, a deductive logic game. 
      I am thinking of a 3-digit number. Try to guess what it is. 
      Here are some clues: 
      When I say:   That means: 
        Pico      One digit is correct but in the wrong position. 
        Fermi     One digit is corret and in the right position. 
        Bagels    No digit is correct. 
     
        I have thought up a number. 
         You have 10 guesses.
      """)

from random import randint
answer = str(randint(1,999))
if len(answer) == 2:
    answer = "0" + answer
elif len(answer) == 1: 
    answer = "00" + answer

answer = "123"
    
num1, num2, num3 = answer[0], answer[1], answer[2]
answers = [num1, num2, num3]

guesses = 1
while guesses <= 10: 
    print(f"Guess #{guesses}")
    while True: 
        try: 
            number = input("Give us a positive 3-digits number: ")
            for i in number: 
                int(i)
            number  = str(number)
            if len(number) < 3 or len(number) > 3: 
                print("Only 3-digits numbers, please!")
                continue
            break
        except ValueError: 
            print("Please, only numbers and positive ones!")
            continue
    
    numbers = [number[0], number[1], number[2]]
    
    count = 0
    
    for i in numbers: 
        if i in answers: 
            if i == answers[number.index(i)]: 
                print("Fermi")
            else: 
                print("Pico")
        else: 
            count +=1
        if count == 3: 
            print("Bagels")

    if numbers == answers: 
        print("You got it!")
        break

    guesses += 1

print("Great job!")