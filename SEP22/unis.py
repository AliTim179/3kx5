#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 11:54:45 2022

@author: alitim179
"""

class myUniversity: 
    def __init__(self): 
        self.name = ""
        self.state = ""
        self.level = ""
        self.students = 0
        self.courses = 0
        self.staff = 0
        
    def uni_info(self): 
        print("Let's define your university with the following details: ")
        self.name = input("Name of your university: ")
        self.state = input("State in which it is located: ")
        self.level = input("University Level: ")
        self.students = int(input("Number of students: "))
        self.courses = int(input("Nunmber of courses: "))
        self.staff = int(input("Number of staff: "))
        info =  (f"Your university is called {self.name}."+ 
                f"\nIt is located in {self.state}."+ 
                f"\nIts level is {self.level}."+ 
                f"\nIt has {self.students} students, {self.courses} courses, and "+ 
                f"{self.staff} people working there.")
        return info
    
my_uni = myUniversity()
print(my_uni.uni_info())


        
        
            
        
