"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
<<<<<<< HEAD
# First example
=======
import math

def add(a, b):
    a + b

def subtract(a, b):
    a - b

def multiply(a, b):
    a * b

def divide(a, b):
    try:
        b / a
    except ZeroDivisionError as e:
        print(e)  # raise ZeroDivisionError if a == 0

def logarithm(a, b):
    try:
        math.log(b) / math.log(a)
    except ValueError as e:
        print(e)
        #use math library + raise ValueError

def exponent(a, b):
    a**b

>>>>>>> 7dedaea0adbe3bea988e751e63348f1ff3303a50

import math

def add(a, b):
    a + b

def sub(a, b):
    a - b

def mul(a, b):
    a * b

def div(a, b):
    try:
        b / a
    except ZeroDivisionError as e:
        print(e)

def log(a, b):
    try:
        math.log(b) / math.log(a)
    except ValueError as e:
        print(e)

def exp(a, b):
    a ** b