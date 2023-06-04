import numpy as np
import math

def funtionsAll(x, ifun):
    match ifun:
        case 1:
            return x * (x * (x + 3) + 2) + 1
        case 2:
            return np.cos(2 * x)
        case 3:
            return 2 * np.sin(x)
        case 4:
            return abs(x)
        case 5:
            return 2 * x + 3

def power(a,x):
    i = 0
    result = 1
    while i < x:
        result *= a
        i += 1
    return result

def factorial(x):
    result = 1
    if x == 0:
        return 1
    if x < 0:
        return 0
    for i in range(1,x):
        result *= i
    return result

def a(x):
    return 1/(math.sqrt(math.pi)*power(2,x)*factorial(x))