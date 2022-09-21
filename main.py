# Marvish Chandra
# Evaluating Lenz's Law (based on the operation of a Gondola)

from re import X
from sympy import *

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