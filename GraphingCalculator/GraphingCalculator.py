"""Graphs a User's Expression.

Function to graph expression collected from user. Takes user input and uses
for loop to iterate through values of x defined in RANGE_LOW and RANGE_HIGH.
Scales to SCALE. Starts by drawing gridlines using the constants below, then
evaluates user input using my_range to increase the resolution of the results.
Technically, the scope of the graph can be changed by reducing the scale and
increasing the labelling on the ticks. 
"""

from math import *

from SimpleGraphics import line, background, text, setFont, setColor, close, ellipse
from MaximaMinima import maxima_minima


X_ZERO = 400        # changes (0, 0) for x
X_MAX = 801         # changes max (0, 0) for x
X_LABEL_START = -13 # first label on x axis
Y_ZERO = 300        # changes (0, 0) for y
Y_MAX = 601         # changes max (0, 0) for y
Y_LABEL_START = 10  # first label on y axis
SCALE = 30          # distance between ticks
LABEL_OFFSET = 10   # distance from gridline to label
X_TICK_RISE = 3     # set width of ticks on x axis (i.e. tick width / 2)
Y_TICK_RISE = 3     # set width of ticks on y axis (i.e. tick width / 2)
RANGE_LOW = -400    # range of x (low)
RANGE_HIGH = 400    # range of x (high)
STEP = 0.1          # custom float iteration step (AKA resolution)

def draw_gridlines():
    """function draws the grid lines using the constants above"""
    background("white")   # set canvas variables
    setFont("Times", "7") # set font variables
    line(0, Y_ZERO, X_MAX, Y_ZERO) ##
    line(X_ZERO, 0, X_ZERO, Y_MAX) # draw x and y axis

    """loop to draw ticks on X axis"""
    x_offset = X_ZERO % SCALE # find remainder to calculate leftover pixels
    x_tick = 0
    x_tick += x_offset
    x_label = X_LABEL_START
    while x_tick <= X_MAX:
        line(x_tick, Y_ZERO - X_TICK_RISE, x_tick, Y_ZERO + X_TICK_RISE)
        if x_label == 0: # skip tick and label when coords == (0, y)
            x_label += 1
            x_tick += SCALE
        else: # draw lables and ticks
            text(x_tick, Y_ZERO + LABEL_OFFSET, x_label)
            x_tick += SCALE
            x_label += 1

    """loop to draw ticks on y axis"""
    y_tick = 0
    y_label = Y_LABEL_START
    while y_tick <= Y_MAX:
        line(X_ZERO - Y_TICK_RISE, y_tick, X_ZERO + Y_TICK_RISE, y_tick)
        if y_label == 0: # skip tick and label when coords == (x, 0)
            y_label -= 1
            y_tick += SCALE
        else: # draw lables and ticks
            text(X_ZERO + LABEL_OFFSET, y_tick, y_label)
            y_tick += SCALE
            y_label -= 1

draw_gridlines()

def my_range(start, end, step):
    """generates a custom range of floats with variable steping needed to
    increase accuracy of function plotting, taken from:
    https://wiki.python.org/moin/ForLoop.
    """
    while start <= end:
        yield start
        start += step

def color_picker(loop_count):
    """picks a color based off number of consecutive loops, the color is chosen
    from the equasion: loop_number % 3 where 0 = Red; 1 = Green; else = Blue.
    """
    color_picker_remainder = loop_count % 3
    if color_picker_remainder == 0:
        setColor("red")
    if color_picker_remainder == 1:
        setColor("green")
    if color_picker_remainder > 1:
        setColor("blue")

def evaluate_expression():
    """function to recieve and process user input, draws the user's expression
    using 100's of tiny SimpleGraphic's line segments.
    """
    line_coordinate_array = [] # set empty array
    tupled_coordinate_array = []
    loop_count = -1 # set loop number to -1 so first run = 0
    # initialize user input, blank line fails to trigger loop
    print("Enter the expression (blank line to quit): ")
    user_input = input("Y = ")

    while user_input != "": # run calculations needed to draw expression
        for x in my_range(RANGE_LOW, RANGE_HIGH, STEP):
            result = eval(user_input)
            # subtract Y_ZERO to center and multiply by SCALE
            y_result = Y_ZERO - (result * SCALE)
            # add X_ZERO to center and multiply by SCALE
            x_result = X_ZERO + (x * SCALE)
            line_coordinate_array.append(x_result)
            line_coordinate_array.append(y_result)

        loop_count += 1
        color_picker(loop_count) # determine line color
        line(line_coordinate_array) # draw curves
        maxima_minima(line_coordinate_array) # calc maxima/minima
        line_coordinate_array = [] # unset array for next run
        print("Enter the expression (blank line to quit): ")
        user_input = input("Y = ")

    if user_input == "":
        close()

evaluate_expression()
