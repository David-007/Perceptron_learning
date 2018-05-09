from __future__ import print_function
import math
#import tensorflow as tf
import numpy as np

#def sig(y):
#	return 1/(1+(math.exp(-y)))

inpt = np.asarray([[0,0],[0,1],[1,0],[1,1]]);
numIn = 4;
desired_out = np.asarray([1,1,1,0]);
bias = -1;
coeff = 0.5;
#rand('state',sum(100*clock));
np.random.seed(1)
weights = 2*np.random.random(4) - 1
iterations = 1000;
out = np.asarray([0.0,0.0,0.0,0.0]);
for i in range(iterations):
     #out = np.asarray([0,0,0,0]);
     for j in range(numIn):
          y = bias*weights[0]+inpt[j][0]*weights[1]+inpt[j][1]*weights[2];
          out[j] = 1/(1+math.exp(-y));
          delta = desired_out[j]-out[j];
          weights[0] = weights[0]+coeff*bias*delta;
          weights[1] = weights[1]+coeff*inpt[j][0]*delta;
          weights[2] = weights[2]+coeff*inpt[j][1]*delta;
ip = np.asarray([[0.1,0.9],[0.8,0.8],[0.95,0.95],[0.2,0.4]]);
op = np.asarray([0.0,0.0,0.0,0.0]);
for i in range(4):
    k = bias*weights[0]+ip[i][0]*weights[1]+ip[i][1]*weights[1];
    op[i]= 1/(1+math.exp(-k))