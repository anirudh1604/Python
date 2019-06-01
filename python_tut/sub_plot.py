import numpy as np
import matplotlib.pyplot as plt
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1=np.arange(0.0,5.0,0.1)
t2=np.arange(0.0,5.0,0.02)

plt.figure(2)
plt.subplot(211)
plt.grid()
plt.plot(t1,f(t1),'b--')
plt.subplot(212)
plt.plot(t2,np.cos(2*np.pi*t2),'r--')
plt.show()