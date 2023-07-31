from math import pi, sqrt, pow, hypot

def f_pi():
    return pi

def f_sqrt(v):
    return sqrt(v)

def f_pow(a, b):
    return pow(a, b)

def f_hypot(x, y):
    return hypot(x, y)

if __name__ == '__main__':
    v = f_pi()
    print(v)