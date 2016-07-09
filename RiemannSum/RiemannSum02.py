#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Date:  28 Jun 2016
@author: DubiousLogik
purpose: evaluate a Riemann Sum for a given function f(x)
         uses 'right' values for the rectangles, i.e. the top right corner of the rectangle 
             touches the function f(x)
         converge to a solution that is within a user-specified error threshold
         error is measured by the distance from one iteration of the sum to the next
         the increment (step value, or dx) is divided by 10 on each iteration
         if the error goes up between iterations an error is thrown (divergence)
"""

from decimal import *
from math import *

def evalF(x):
    #return x**2
    #return 5
    #return x
    return Decimal(sqrt(x))

def RangeOfRightSteps(start, end, step):
    while (start+step) <= end:
        start += step
        yield start

def RiemannSumRight(limitLow, limitHigh, increment):
    sum = 0
    incrementCount = 0
    for i in RangeOfRightSteps(limitLow, limitHigh, increment):
        incrementCount += 1
        sum = sum + (evalF(i)*increment)
    #print "\tRIGHT>> lastIncrement = {}, incrementCount = {}, thisIncrement {}".format(lastIncrement, incrementCount, thisIncrement)
    return sum

def ConvergeToSum(limitLow, limitHigh, initialIncrement, errorThreshold):
    increment = initialIncrement
    right = RiemannSumRight(limitLow, limitHigh, increment)
    previousRight = 0
    previousDelta = right
    observedDelta = abs(right - previousRight)

    while(observedDelta > errorThreshold):
        right = RiemannSumRight(limitLow, limitHigh, increment)
        observedDelta = abs(right - previousRight)
        print "right {}, previousRight {}, increment {}, dist from prev {}, errorThreshold {}".format(right, previousRight, '{0:.3g}'.format(increment), observedDelta, '{0:.3g}'.format(errorThreshold))
        if(observedDelta > previousDelta):
            print "Divergence detected, observedDelta = {}, previousDelta = {}".format(observedDelta, previousDelta)
            return 0
        increment = increment/10
        previousDelta = observedDelta
        previousRight = right
            
    print ""
    return right        

if __name__ == "__main__" :
    #ensure this is large enough to handle the error threshold below; 
    #if divergence is detected, first try increasing the precision
    getcontext().prec = 8
    a = Decimal(0)
    b = Decimal(10)
    increment = Decimal(0.1)
    error = Decimal(0.01)
    print ""
    print "== Starting ====================================================="
    print "f(x) output: x={}, f(x)={}".format(b, evalF(b))
    print "== Convergence ======================================================"
    print ""
    print "ConvergeToSum({}, {}, {}) = {}".format(a, b, '{0:.3g}'.format(error), ConvergeToSum(a, b, increment, error))
    print ""
    print "== End =="