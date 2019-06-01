import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
t=np.arange(0.,5.,0.2)
plt.plot(t,t**2,'b--',label='^2')
plt.plot(t,t**2.2,'rs',label='^2.2')
plt.plot(t,t**2.5,'g^',label='^2.5')
plt.grid()
#plt.legend()
plt.show()

x1=[1,2,3,4]
x2=[1,2,3,4]
y1=[1,4,9,16]
y2=[2,4,6,8]
lines=plt1.plot(x1,y1,x2,y2
)
plt1.setp(lines[0],color='g',linewidth=2.0)
plt1.show()