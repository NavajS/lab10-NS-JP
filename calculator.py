# https://github.com/NavajS/lab10-NS-JP
# Partner 1: Jenish Patel
# Partner 2: Navaj Sivakumar

import math

def square_root(a):
    try:
        math.sqrt(a)
    except ValueError as e:
        print(e)

def hypotenuse(a, b):
    math.hypot(a, b)

def logarithm(a, b):
    try:
        math.log(b) / math.log(a)
    except ValueError as e:
        print(e)
        #use math library + raise ValueError

import math

def add(a, b):
    a + b

def subtract(a, b):
    a - b

def mul(a, b):
    a * b

def div(a, b):
    try:
        b / a
    except ZeroDivisionError as e:
        print(e)


def exp(a, b):
    a ** b
