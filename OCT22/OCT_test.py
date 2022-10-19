#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 12:52:21 2022

@author: alitim179
"""

nyear = int(input())

while True:     
    for i in list(str(nyear)): 
        if list(str(nyear)).count(i) > 1: 
            break
        nyear = "".join(list(str(nyear)))

    if type(nyear) == str: 
        print(nyear)
        break

    nyear += 1





