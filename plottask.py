# plottask.py 
# A program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 
# in the range [0, 4] on the one set of axes.
# Author: Laura Condon

# import the required modules - numpy and matplotlib
# Use 'as' to shorten how they are called in the program
import numpy as np
import matplotlib.pyplot as plt

# specifies what font style to use for all text in the plot
plt.rcParams['font.family'] = 'Courier New'

# defines the range of values for x on the graph
x = np.arange(0, 4)
# defines the values of the functions to be plotted
f = x 
g = x**2
h = x**3

# displays a grid and specifies its style
plt.rc('grid', linestyle='dotted', color='gray', alpha=0.7)
plt.grid()

# calls the plot command, individually for each line to be plotted
# specifies the color, style of, width and label of each line
plt.plot(f, color = '#006ba4', linestyle='solid', linewidth=3.0, label='f(x)')
plt.plot(g, color = '#ff800e', linestyle='dashed', dashes=(4, 2), linewidth=3.0, label='g(x)')
plt.plot(h, color = '#595959', linestyle='dashed', dashes=(2, 1),linewidth=3.0, label='h(x)')  

# specifies the name for each axis and for the title
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('plot of f(x), g(x) and h(x)')
# displays a legend
plt.legend()

# displays the resulting graph
plt.show()

