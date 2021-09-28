import matplotlib.pyplot as plt;
import numpy as np;

#Setup: 3 snails chase each other, starting from the 3 vertices of a equilateral triangle moving always towards their target snail respectively. Triangle length 60, snail velocity 5/s.
#Q: how long does it take for them to meet?
#A: By considering this problem in polar coordinate, it is easy to see that their paths all follow a logrithmic polar curve, thus calculate the curve length then divide by speed gives the answer.
#However, these codes wants to solve the problem by programming.

a_x_0 = 0; a_y_0 = 0; b_x_0 = 60; b_y_0 = 0; c_x_0 = 30; c_y_0 = 30*np.sqrt(3); #since sqrt is undefined here, meant to be sqrt(3).

path_a = []; path_b = []; path_c = [];
a_x = []; a_y = []; b_x = []; b_y = []; c_x = []; c_y = [];

dt = 0; v = 5;
    
def newposition(x1, y1, x2, y2, dt):
    l = v*dt;
    L = np.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
    x1_new = x1 + (x2-x1)*l/L;
    y1_new = y1 + (y2-y1)*l/L;
    return(x1_new, y1_new)

path_a.append((a_x_0,a_y_0)); a_x.append(a_x_0); a_y.append(a_y_0);
path_a.append(newposition(a_x_0, a_y_0, b_x_0, b_y_0, 1/100)); #a goes to b
a_x.append(path_a[1][0]); a_y.append(path_a[1][1]);
path_b.append((b_x_0,b_y_0)); b_x.append(b_x_0); b_y.append(b_y_0);
path_c.append((c_x_0,c_y_0)); c_x.append(c_x_0); c_y.append(c_y_0);

for t in range(0,800,1):
    dt = 1/100;
    
    #c goes to a
    path_c.append(newposition(path_c[t][0], path_c[t][1], path_a[t+1][0], path_a[t+1][1], dt));
    c_x.append(path_c[t+1][0]);
    c_y.append(path_c[t+1][1]);
    
    #b goes to c
    path_b.append(newposition(path_b[t][0], path_b[t][1], path_c[t+1][0], path_c[t+1][1], dt));
    b_x.append(path_b[t+1][0]);
    b_y.append(path_b[t+1][1]);
    
    #a goes to b
    path_a.append(newposition(path_a[t+1][0], path_a[t+1][1], path_b[t+1][0], path_b[t+1][1], dt));
    a_x.append(path_a[t+2][0]);
    a_y.append(path_a[t+2][1]);
    
    
plt.plot(a_x,a_y)
plt.plot(b_x,b_y)
plt.plot(c_x,c_y)

print(path_a)
