# plottask.py 
# A program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 
# in the range [0, 4] on the one set of axes.
# Author: Laura Condon

# import the required modules - numpy and matplotlib
# Use 'as' to shorten how you refer to them in the program
import numpy as np
import matplotlib.pyplot as plt

# define the range of values for x on the graph
x = np.arange(0, 4)
# define the values of the functions to be plotted
f = x 
g = x**2
h = x**3

# call the plot command, individually for each line to be plotted
# I used the tableau color blind 10 palette to choose colours for my lines
# converted them from rgb to hex for easier entry
plt.plot(f, color = '#006ba4', linewidth=3.0)
plt.plot(g, color = '#ff800e', linewidth=3.0)
plt.plot(h, color = '#595959', linewidth=3.0)  
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