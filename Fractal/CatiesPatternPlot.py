#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: DubiousLogik
Date:  11 March 2016
'''
import math
import matplotlib.pyplot as pl
from pylab import savefig
from pylab import axis
from decimal import *

def print_stats(n):
    getcontext().prec = 6
    limit = compute_limits(n) 
    area = compute_area(n,4)
    coverage = Decimal(0.0)
    coverage = Decimal(area)/Decimal(limit**2)
    print 'current n={}, side length={}, pattern area={}, total area={}, coverage={}'.format(n,limit,area,limit**2,coverage)
	
def draw_pattern(n):
    #compute limits, set axis limits, draw squares in recursive loop
    limit = compute_limits(n) #limit = size of 1 side of the white canvas square we will draw on
    area = compute_area(n,4)
    coverage = Decimal(0.0)
    coverage = Decimal(area)/Decimal(limit**2)
    print 'current n={}, side length={}, pattern area={}, total area={}, coverage={}'.format(n,limit,area,limit**2,coverage)

    center = limit/2 #int(math.ceil(limit/2))
        
    fig1 = pl.gcf()
    ax = pl.axes(xlim=(0,limit), ylim=(0,limit))
    ax.set_aspect('equal')
    
    #draw central square
    side = 2**n
    halfside = side/2 #int(math.ceil(side/2))
    start = center - halfside #starting point is lower left (southwest) corner
    square = draw_square(start,start, start+side, start, start+side, start+side, start, start+side)
    ax.add_patch(square)
    if n>0 :
        nextSide = 2**(n-1)
        x_corners = [start-nextSide, start+side, start+side, start-nextSide]
        y_corners = [start-nextSide, start-nextSide, start+side, start+side]
        draw_nextlayer(ax, n-1, x_corners, y_corners, len(x_corners))
    pl.show()
    fig1.savefig('c:\\temp\\samplePlot{}.png'.format(n), dpi=360) #,dpi='120',facecolor='black', edgecolor='white')

def compute_limits(n):
    if n<0 : return 0
    currentLimit = (2**n) 
    nextLimit = compute_outer_limits(n-1)
    return currentLimit+(nextLimit*2)

def compute_outer_limits(n):
    if n<0 : return 0
    return (2**n)+compute_outer_limits(n-1)

def compute_area(n,fc):
    """
    Compute area for Catie's pattern given sequence number n, an integer and fc, the number of free corners that you start with (4)
    On the first pass fc=4, it is 3 on all subsequent passes since 1 vertex (corner) is taken on every new square where it connects to the larger square
    """
    if n<0 : return 0
    return (2**n)**2 + fc*(compute_area(n-1, 3))

def draw_square(swX, swY, seX, seY, neX, neY, nwX, nwY):
    #coordinates naming convention:  southwest corner X = swX, southwest corner Y = swY, etc
    #proceed counterclockwise from sw corner: sw -> se -> ne -> nw
    global count
    count += 1
    square = pl.Polygon([(swX, swY),(seX, seY),(neX,neY),(nwX, nwY)],closed=True)
    return square
    
def draw_nextlayer(ax, n, x_corners, y_corners, freecorners):
    if n<0 : return
    side = 2**n
    for i in range(0, freecorners):
        if x_corners[i]== -1 : 
            continue
        else :
            nextSquare = draw_square(x_corners[i], y_corners[i], x_corners[i]+side, y_corners[i], x_corners[i]+side, y_corners[i]+side, x_corners[i], y_corners[i]+side)
            ax.add_patch(nextSquare)
            if n>-1 : 
                nextSide = 2**(n-1)
                halfside = nextSide/2
                startNextX = x_corners[i]
                startNextY = y_corners[i]
                xNext_corners = [0,0,0,0]
                yNext_corners = [0,0,0,0]

                if i==0 : #sw orientation, skip ne
                    xNext_corners = [startNextX-nextSide, startNextX+side, -1, startNextX-nextSide]
                    yNext_corners = [startNextY-nextSide, startNextY-nextSide, -1, startNextY+side]
                if i==1 : #se orientation, skip nw
                    xNext_corners = [startNextX-nextSide, startNextX+side, startNextX+side, -1]
                    yNext_corners = [startNextY-nextSide, startNextY-nextSide, startNextY+side, -1]
                if i==2 : #ne orientation, skip sw
                    xNext_corners = [-1, startNextX+side, startNextX+side, startNextX-nextSide]
                    yNext_corners = [-1, startNextY-nextSide, startNextY+side, startNextY+side]
                if i==3 : #nw orientation, skip se
                    xNext_corners = [startNextX-nextSide, -1, startNextX+side, startNextX-nextSide]
                    yNext_corners = [startNextY-nextSide, -1, startNextY+side, startNextY+side]
                draw_nextlayer(ax, n-1, xNext_corners, yNext_corners, len(xNext_corners))
 
if __name__ == '__main__':
    global count
    
    #draw_pattern(11)
    #for i in range(0,110):
    #    print_stats(i)
    for j in range(7,8):
        count = 0
        draw_pattern(j)
        print 'count of squares drawn = {}'.format(count)
        