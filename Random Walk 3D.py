import matplotlib as mpl;
import matplotlib.pyplot as plt;
from mpl_toolkits.mplot3d import axes3d;
import random as random;
fig = plt.figure()
ax = fig.gca(projection='3d')

def randomwalk(k,l,m):
        x0 = 0;
        y0 = 0;
        z0 = 0;
        
        currx = x0;
        curry = y0;
        currz = z0;
        
        outx = [];
        outy = [];
        outz = [];
        path = [];
        
        while abs(currx) <= k and abs(curry) <= l and abs(currz) <= m:
            outx.append(currx);
            outy.append(curry);
            outz.append(currz);
            currx = currx + random.choice([-1,0,1]);
            curry = curry + random.choice([-1,0,1]);
            currz = currz + random.choice([-1,0,1]);
        
        for i in range(len(outx)):
            path.append([outx[i],outy[i],outz[i]])
        
        print(path);            
        
        for i in range(0,len(outx)-1):
            ax.plot((outx[i],outx[i+1]),(outy[i],outy[i+1]),(outz[i],outz[i+1]))
        

randomwalk(40,30,40)    
