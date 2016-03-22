#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Date:  18 Feb 2016
@author: DubiousLogik
"""

import numpy as np

def computeArea(n, fc):
    """
    Compute area for Catie's pattern given sequence number n, an integer
    and fc, the number of free corners that you start with (4)
    On the first pass fc=4, it is 3 on all subsequent passes since 1 vertex (corner)
    is taken on every new square where it connects to the larger square
    """
    if n<0 : return 0
    return (2**n)**2 + fc*(computeArea(n-1, 3))
    
if __name__ == "__main__":

    freeCorners = 4
    n = 0
    print 'For n = {} the area is {}'.format(n,computeArea(n, freeCorners))
    n = 1
    print 'For n = {} the area is {}'.format(n,computeArea(n, freeCorners))
    n = 2
    print 'For n = {} the area is {}'.format(n,computeArea(n, freeCorners))
    n = 3
    print 'For n = {} the area is {}'.format(n,computeArea(n, freeCorners))
    n = 4
    print 'For n = {} the area is {}'.format(n,computeArea(n, freeCorners))    
    n = 5
    print 'For n = {} the area is {}'.format(n,computeArea(n, freeCorners))    
    