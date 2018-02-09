#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Date:  07 Feb 2018

import numpy as np

def DivBySevenprocess(n):
    d = n % 10
    temp1 = (n - d) / 10
    nextN = temp1 - 2*d
    print 'n = {}, temp1 = {}, nextN = {}'.format(n, temp1, nextN)
    if nextN < 0 : return n % 7
    return DivBySevenprocess(nextN)
    
if __name__ == "__main__":
    n = 4501
    print 'For n = {} the result is {}'.format(n,DivBySevenprocess(n))
    n = 4502
    print 'For n = {} the result is {}'.format(n,DivBySevenprocess(n))
    n = 34502
    print 'For n = {} the result is {}'.format(n,DivBySevenprocess(n))