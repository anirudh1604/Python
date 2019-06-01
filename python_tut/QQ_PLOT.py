import numpy as np
import pylab
import scipy.stats as stats
std_normal = np.random.normal (loc=0,scale=1.0,size=100)
for i in range (0,101):
    print (i,np.percentile(std_normal,i))

measurements =  np.random.normal (loc=5,scale=20.0,size=100)
stats.probplot(measurements,dist='norm',plot=pylab)
pylab.show()