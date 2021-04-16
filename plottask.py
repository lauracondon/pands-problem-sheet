# plottask.py 
# A program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 
# in the range [0, 4] on the one set of axes.
# Author: Laura Condon

# import the required modules - numpy and matplotlib
# Use 'as' to shorten how they are called in the program
import numpy as np
import matplotlib.pyplot as plt

# specifies what font style to use for all text in the plot [1]
plt.rcParams["font.family"] = 'DejaVu Sans'

# defines the range of values for x on the graph [2]
x = np.arange(0, 4) 
# defines the values of the functions to be plotted
f = x 
g = x**2
h = x**3

# displays a grid and specifies its style [3]
plt.rc("grid", linestyle = "dotted", color = "gray", alpha=0.7)
plt.grid()

# calls the plot command, individually for each line to be plotted [4]
# the style of each line is specified using a variety of attributes [5][6][7]
plt.plot(f, color = "#006ba4", linestyle = "solid", linewidth = 3.0, label= "f(x)")
plt.plot(g, color = "#ff800e", linestyle = "dashed", dashes = (4, 2), linewidth = 3.0, label= "g(x)")
plt.plot(h, color = "#595959", linestyle = "dashed", dashes = (2, 1),linewidth = 3.0, label= "h(x)")  

# specifies the name for each axis and for the title [8]
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("plot of f(x), g(x) and h(x)")
# displays a legend 
plt.legend()

# saves graph to plottask.png
plt.savefig("plottask.png")
# displays the resulting graph
plt.show()

# References 
# [1] https://stackoverflow.com/questions/43814540/how-to-change-the-font-of-the-legend (accessed 22/03/2021)
# [2] https://realpython.com/how-to-use-numpy-arange/ (accessed 10/03/2021)
# [3] https://stackoverflow.com/questions/8209568/how-do-i-draw-a-grid-onto-a-plot-in-python (acessed 22/03/2011)
# [4] https://www.kite.com/python/answers/how-to-plot-multiple-lines-on-the-same-graph-in-matplotlib-in-python (accessed 10/03/2021)
# [5] https://public.tableau.com/profile/chris.gerrard#!/vizhome/TableauColors/ColorPaletteswithRGBValues (accessed 20/03/2021)
# [6] https://matplotlib.org/stable/gallery/lines_bars_and_markers/line_demo_dash_control.html (accessed 22/03/2021)
# [7] https://matplotlib.org/stable/gallery/index.html (accessed 20/03/2021)
# [8] https://jakevdp.github.io/PythonDataScienceHandbook/04.01-simple-line-plots.html (accessed 22/03/2021)

