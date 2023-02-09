#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 15:18:37 2019

@author: pom5109
"""

def main():
    number = int(input('Enter a non negative integer: '))
    
    fact = factorial(number)
    
    print('the factorial of', number, 'is: ', fact)
    
    
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)
    
main()
    
    