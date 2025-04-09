# https://github.com/NavajS/lab10-NS-JP
# Partner 1: Jenish Patel
# Partner 2: Navaj Sivakumar

import math

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError
    return math.log(b) / math.log(a)
        #use math library + raise ValueError

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b


def exp(a, b):
    return a ** b
