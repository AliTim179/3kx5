#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 12:29:06 2022

@author: alitim179
"""
from unis import myUniversity

class Student: 
    def __init__(self): 
        self.full_name = ""
        self.age = 0
        self.major = ""
        self.GPA = 0
    
    def stud_info(self):
        print("Let's get to know each other! Tell us about yourself: ")
        self.full_name = input("What is your full name: ")
        self.age = int(input("How old are you: "))
        self.major = input("What is your major: ")
        self.GPA = int(input("What is your GPA: "))
        info = (f"\nYou are {self.full_name}, {self.age} yo "+
                f"\nYour major is {self.major} with GPA {self.GPA}.")
        print(info)
        
        def Yes_no(): 
            yes_no = input("Is everything correct? Yes or No? ")
            while True: 
                if yes_no.lower() == "no":
                    print("Okay, let's fix that!")
                    break
                elif yes_no.lower() == "yes": 
                    print("Great! You are welcome!\n")
                    break
                else: 
                    print("Please, only 'yes' or 'no'...")
                    yes_no = input("Is everything correct? Yes or No? ")
                
            while yes_no.lower() != "yes":
                print(info)
                print("\nWhat information you'd like to change? One at a time, please!")
                change = int(input("Press '1' to change your full name"+
                               "\nPress '2' to change your age"+
                               "\nPress '3' to change your major"+
                               "\nPress '4' to change your GPA"+
                               "\nPress '0' if you changed your mind or you've done: "))
            
                if change == 1: 
                    self.full_name = input("What is your full name: ")                  
                    print(self.full_name)
                elif change == 2: 
                    self.age = int(input("How old are you: "))
                    print(self.age)
                elif change == 3: 
                    self.major = input("What is your major: ")
                    print(self.major)
                elif change == 4: 
                    self.GPA = int(input("What is your GPA: "))
                    print(self.GPA)
                elif change == 0: 
                    yes_no = "yes"
                else: 
                    print("Please, only from 0 to 4...")
            print(self.full_name)        
            print(self.age)
            print(self.major)        
            print(self.GPA)        
            print(info)
            
        Yes_no()
    
at179 = Student()
at179.stud_info()













    