import numpy as np
import matplotlib.pyplot as plt
def f(t):
   return 2*np.cos(t)+2015
def g(t):
   return t+1997
t1 = np.arange(0.0, 20.0, 0.3)
plt.figure(3)
plt.subplot(211)
plt.plot(t1, f(t1), '*c', t1, g(t1), 'y')
plt.subplot(212)
plt.plot(t1, f(t1), 'bo')
plt.savefig('p3.png')

