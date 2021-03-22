# plottask.py 
# A program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 
# in the range [0, 4] on the one set of axes.
# Author: Laura Condon

# import the required modules - numpy and matplotlib
# Use 'as' to shorten how you refer to them in the program
import numpy as np
import matplotlib.pyplot as plt

# specify what font style to use for all text in the plot
plt.rcParams['font.family'] = 'Courier New'

# define the range of values for x on the graph
x = np.arange(0, 4)
# define the values of the functions to be plotted
f = x 
g = x**2
h = x**3

# display a grid and specify its style
plt.rc('grid', linestyle='dotted', color='gray', alpha=0.7)
plt.grid()

# call the plot command, individually for each line to be plotted
# specify the color, style of, width and label for each line
plt.plot(f, color = '#006ba4', linestyle='solid', linewidth=3.0, label='f(x)')
plt.plot(g, color = '#ff800e', linestyle='dashed', dashes=(4, 2), linewidth=3.0, label='g(x)')
plt.plot(h, color = '#595959', linestyle='dashed', dashes=(2, 1),linewidth=3.0, label='h(x)')  

# specify the name for each axis and for the title
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('plot of f(x), g(x) and h(x)')
# display a legend
plt.legend()

# show command will display the resulting graph
plt.show()

#References: 
# https://realpython.com/tutorials/numpy/ (accessed 10/03/2021)
# https://realpython.com/how-to-use-numpy-arange/ (accessed 10/03/2021)
# https://www.tutorialspoint.com/matlab/matlab_plotting.htm (accessed 10/03/2021)
# https://www.kite.com/python/answers/how-to-plot-multiple-lines-on-the-same-graph-in-matplotlib-in-python(accessed 10/03/2021)

# https://www.rgbtohex.net/rgb/ (accessed 20/03/2021)
# https://public.tableau.com/profile/chris.gerrard#!/vizhome/TableauColors/ColorPaletteswithRGBValues (accessed 20/03/2021)
# https://matplotlib.org/stable/gallery/index.html (accessed 20/03/2021)

# https://matplotlib.org/stable/gallery/lines_bars_and_markers/line_demo_dash_control.html (accessed 22/03/2021)
# https://stackoverflow.com/questions/43814540/how-to-change-the-font-of-the-legend (accessed 22/03/2021)
# https://pythonbasics.org/matplotlib-line-chart/ (accessed 22/03/2021)
# https://jakevdp.github.io/PythonDataScienceHandbook/04.01-simple-line-plots.html (accessed 22/03/2021)
# https://stackoverflow.com/questions/8209568/how-do-i-draw-a-grid-onto-a-plot-in-python (acessed 22/03/2011)
