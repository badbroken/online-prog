import math


def ang(a, b):
    c = math.degrees(math.atan(a / b))
    print(round(c), "\xb0", sep='')


a = int(input())
b = int(input())
ang(a, b)
