from math import factorial
import numpy as np
# 1. digital algorithm
def DigitalAlgo(order: int, ctrlPts, t: float):
    res: type(ctrlPts[0])
    for i in range(len(ctrlPts)):
        res += (factorial(order) / (factorial(t) * factorial(order - i))) * (
                    t ** i) * (1 - t) ** (order - i) * ctrlPts[i]
    return res

#2. De Casteljau algorithm
def DeCasteljauAlgo(order: int, ctrlPts, t: float):
    res: float = 0.0
    temp = ctrlPts
    for i in range(0, order):
        for j in range(0, order - i):
            temp[j] = (1.0 - t) * temp[j] + t * temp[j + 1]
    return temp[0]


# evaluates cubic bezier with control points at t, return point
def cb(ctrlPts, t):
    return (1.0-t) ** 3 * ctrlPts[0] + 3 * (1.0 - t) ** 2 * t * ctrlPts[1] + 3 * (1.0 - t) * t ** 2 * ctrlPts[2] + t ** 3 * ctrlPts[3]


# evaluates cubic bezier first derivative at t, return point
def cb_dev(ctrlPts, t):
    return 3*(1.0-t)**2 * (ctrlPts[1]-ctrlPts[0]) + 6*(1.0-t) * t * (ctrlPts[2]-ctrlPts[1]) + 3*t**2 * (ctrlPts[3]-ctrlPts[2])


# evaluates cubic bezier second derivative at t, return point
def cb_dev2(ctrlPts, t):
    return 6*(1.0-t) * (ctrlPts[2]-2*ctrlPts[1]+ctrlPts[0]) + 6*(t) * (ctrlPts[3]-2*ctrlPts[2]+ctrlPts[1])


