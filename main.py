# Marvish Chandra
# Evaluating Lenz's Law (based on the operation of a Gondola)

from re import L, X
from sympy import *
import math


x = Symbol ("x")
t = Symbol("t")

f = x 
g = t 

derivF = f.diff(x)
derivG = f.diff(t)

def gondolaLaw(N):
    -N * (derivF / derivG)

def finding_linear_speed(w,r,v):
# finding revolutions
    assert newW == w * (2 * 3.14) / 1

assert v == (r * newW) * (60 / 1) # converting to mi/hr

# calculating cable tension, assuming no equilibirum b/c of no acceleration

class secondTension:
    def secondxDirection(T2):
        T2 * math.degrees(cos(35))
    def secondyDirection(T2):
        T2 * math.degrees(sin(35))
class firstTension:
    def firstxDirection(T1):
        T1 * math.degrees(cos(40))
    def firstyDirection(T2):
        T2 * math.degrees(sin(40))

def resultingTensions(): # divide results based from above classes
    # def secondxDirection(T2) / def firstxDirection(T2)
    # assert 0 == def secondyDirection(T1) - def firstyDirection(T1) - 25,000 
    
    def thirdTension(T2,T1):
        T2 - T1
