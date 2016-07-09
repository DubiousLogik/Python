#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Date:  28 Jun 2016
@author: DubiousLogik
purpose: evaluate a Riemann Sum for a given function f(x)
         evaluate both 'left' and 'right' values (rectangles) for each iteration
         converge to a solution that is within a user-specified error threshold
         solution is the mean of the 2 values (right + left)/2
         error is measured by distance to the midpoint between left and right 
             (i.e. where the mean would be): abs(right - left)/2
         the increment (step value, or dx) is divided by 10 on each iteration
         if the error goes up between iterations an error is thrown (divergence)
"""

from decimal import *
from math import *

def evalF(x):
    #return x**2
    return 5
    #return x
    #return Decimal(sqrt(x))

def RangeOfLeftSteps(start, end, step):
    while (start+step) <= end:
        yield start
        start += step

def RangeOfRightSteps(start, end, step):
    while (start+step) <= end:
        start += step
        yield start
        
def RiemannSumLeft(limitLow, limitHigh, increment):
    sum = 0
    lastIncrement = 0
    incrementCount = 0
    for i in RangeOfLeftSteps(limitLow, limitHigh, increment):
        thisIncrement = i - lastIncrement
        lastIncrement = i
        incrementCount += 1
        sum = sum + (evalF(i)*thisIncrement)
    #print "\tLEFT>> lastIncrement = {}, incrementCount = {}, thisIncrement {}".format(lastIncrement, incrementCount, thisIncrement)
    return sum

def RiemannSumRight(limitLow, limitHigh, increment):
    sum = 0
    lastIncrement = 0
    incrementCount = 0
    for i in RangeOfRightSteps(limitLow, limitHigh, increment):
        thisIncrement = i - lastIncrement
        lastIncrement = i
        incrementCount += 1
        sum = sum + (evalF(i)*thisIncrement)
    #print "\tRIGHT>> lastIncrement = {}, incrementCount = {}, thisIncrement {}".format(lastIncrement, incrementCount, thisIncrement)
    return sum

def ConvergeToSum(limitLow, limitHigh, errorThreshold):
    increment = Decimal(0.1)
    left = RiemannSumLeft(limitLow, limitHigh, increment)
    right = RiemannSumRight(limitLow, limitHigh, increment)
    mean = Decimal((left + right)/2)
    observedError = abs(left - right)/2
    previousError = 0
    print "left {}, right {}, mean {}, dist to mean {}, increment {}".format(left, right, mean, observedError, '{0:.3g}'.format(increment))

    while(observedError > errorThreshold):
        increment = increment/10
        left = RiemannSumLeft(limitLow, limitHigh, increment)
        right = RiemannSumRight(limitLow, limitHigh, increment)
        mean = Decimal((left + right)/2)
        previousError = observedError
        observedError = abs(left - right)/2
        print "left {}, right {}, mean {}, dist to mean {}, increment {}".format(left, right, mean, observedError, '{0:.3g}'.format(increment))
        if(observedError > previousError):
            print "Divergence detected, observedError = {}, previousError = {}".format(observedError,previousError)
            return 0
    
    print ""
    return mean        

if __name__ == "__main__" :
    getcontext().prec = 8
    a = Decimal(0)
    b = Decimal(1)
    #testIncrement = Decimal(0.1)
    error = Decimal(0.001)
    print ""
    print "== Starting ====================================================="
    print "f(x) output: x={}, f(x)={}".format(b, evalF(b))
    #print "\tRiemannSumLeft({}, {}, {}) = {}".format(a, b, '{0:.3g}'.format(testIncrement), RiemannSumLeft(a, b, testIncrement))
    #print "\tRiemannSumRight({}, {}, {}) = {}".format(a, b, '{0:.3g}'.format(testIncrement), RiemannSumRight(a, b, testIncrement))
    print "== Convergence ======================================================"
    print ""
    print "ConvergeToSum({}, {}, {}) = {}".format(a, b, '{0:.3g}'.format(error), ConvergeToSum(a, b, error))
    print ""
    print "== End =="