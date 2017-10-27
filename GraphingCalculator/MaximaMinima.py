"""Program to find the local minima/maxima of an coordinate array.

Step one of this program uses list segments to separate the x and y coordinates
in the list passed thru this function's call. Then, using a while loop, the
program iterates through all of the items in the split lists to find the maxima
and minima--the logic is pretty self-explanitory if you look at the loop.

For the second step, elipses are drawn using a for loop on the maxima / minima
arrays. If x == 0, no ellipse is drawn.

I devised these methods from various sections of the python documentation, as
this solution took me many days to work out, I lost track of all my sources. I
wrote this final form of the program with no outside reference.
"""

from  SimpleGraphics import ellipse, setColor


X_ZER0 = 400    # x + X_ZERO = (0, y)
X_OFFSET = 1    # used to account for rounding errors
Y_ZERO = 300
Y_OFFSET = 1
ELLIPSE_W_H = 6 # width and height of the ellipse markers

def maxima_minima(array):
    """function to split an array of coordinates and find the maxima/minima"""

    x_array = array[0::2] # finds all values for x
    y_array = array[1::2] # finds all values for y
    minima_array = []     ##
    maxima_array = []     # set empty arrays

    pos = 0 # position variable to index array position, begins with first x

    # limit loop to lenght of x_array (- 1 to skip last value and avoid scope
    # errors)
    while pos < len(x_array) - 1:

        # find minima
        if y_array[pos] > y_array[pos - 1] and y_array[pos] > y_array[pos + 1]:
            coordinate = x_array[pos], y_array[pos]
            minima_array.append(coordinate)
            pos += 1

        # find maxima
        if y_array[pos] < y_array[pos - 1] and y_array[pos] < y_array[pos + 1]:
            coordinate = x_array[pos], y_array[pos]
            maxima_array.append(coordinate)
            pos += 1

        # move to next item if no maxima/minima coordinate found
        else:
            pos += 1

    for item in maxima_array: # draw the maxima
        x, y = item
        # skip ellipse when coordinates = (0, 0) (offset coorects for rounding)
        if round(x) != (X_ZER0 + X_OFFSET) or round(y) != (Y_ZERO + Y_OFFSET):
            x -= (ELLIPSE_W_H / 2) ##
            y -= (ELLIPSE_W_H / 2) # account for width/height of ellipse
            setColor("purple")
            ellipse(x, y, ELLIPSE_W_H, ELLIPSE_W_H)

    for item in minima_array: # draw the minima
        x, y = item
        # skip ellipse when coordinates = (0, 0) (offset coorects for rounding)
        if round(x) != (X_ZER0 + X_OFFSET) or round(y) != (Y_ZERO + Y_OFFSET):
            x -= (ELLIPSE_W_H / 2) ##
            y -= (ELLIPSE_W_H / 2) # account for width/height of ellipse
            setColor("orange")
            ellipse(x, y, ELLIPSE_W_H, ELLIPSE_W_H)
