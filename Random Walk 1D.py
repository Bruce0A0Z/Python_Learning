
#import pdfkit
import matplotlib.pyplot as plt;
import random as random;

def randomwalk(k):
        x0 = 0;

        currx = x0;
        
        outx = [];

        while abs(currx) <= k:
            outx.append(currx);
            currx = currx + random.choice([-1,0,1]);
                 
        print(outx);            
        
        for i in range(0,len(outx)-1):
            plt.plot((i,i+1),(outx[i],outx[i+1]))
        
randomwalk(50)    

#pdfkit.from_file('xxx.html','file_test.pdf',configuration=config)　　#Generate in file
