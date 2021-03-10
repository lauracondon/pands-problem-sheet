# plottask.py 
# A program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 
# in the range [0, 4] on the one set of axes.
# Author: Laura Condon

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 4)
f = x 
g = x**2
h = x**3
plt.plot(f)
plt.plot(g)
plt.plot(h)
plt.show()



#References: 
# https://realpython.com/tutorials/numpy/ (accessed 10/03/2021)
# https://realpython.com/how-to-use-numpy-arange/ (accessed 10/03/2021)
# https://www.tutorialspoint.com/matlab/matlab_plotting.htm (accessed 10/03/2021)
# https://www.kite.com/python/answers/how-to-plot-multiple-lines-on-the-same-graph-in-matplotlib-in-python(accessed 10/03/2021)