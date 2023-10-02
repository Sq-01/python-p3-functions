#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name="Guido"):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default("Guido")

def add(num1 = 45, num2 = 55):
    return num1 + num2

def halve(number):
    #number = 100
    return number / 2

""" def halve(number):
    number = 99
    return number / 2 """