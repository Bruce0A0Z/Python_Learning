# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt;
import random as random;

def randomwalk(k,l):
        x0 = 0;
        y0 = 0;
        
        currx = x0;
        curry = y0;
        
        outx = [];
        outy = [];
        path = [];
        
        while abs(currx) <= k and abs(curry) <= l:
            outx.append(currx);
            outy.append(curry);
            currx = currx + random.choice([-1,0,1]);
            curry = curry + random.choice([-1,0,1]);
        
        for i in range(len(outx)):
            path.append([outx[i],outy[i]])
        
        print(path);            
        
        for i in range(0,len(outx)-1):
            plt.plot((outx[i],outx[i+1]),(outy[i],outy[i+1]))
        

randomwalk(30,50)    
