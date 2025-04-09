"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

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