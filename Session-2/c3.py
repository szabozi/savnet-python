import numpy as np


def circle_area1(r):
    return np.pi * (r ** 2)


def circle_area2(r):
    return np.pi * r ** 2


print(circle_area1(4))
print(circle_area2(4))
