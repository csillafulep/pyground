''' python playground Csincsi <3 Mate '''

import numpy as np
import matplotlib.pyplot as plt
from point import *

p = Point(1, 2)

print(p.x, p.y)

plt.figure(1)
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')

plt.figure(2)
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()
