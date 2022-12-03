from matplotlib import pyplot as plt
import numpy as np

# Name: Mario A. Garza

# Create a plot of the function y = 8 * sinc(x)
# Include a proper title, axis labels, legend, and a grid
# Customize the color and style for the line
# HINT: line styles include the following [ '-' | '--' | '-.' | ':' | 'steps' | ...] and are included in
#       the same string as the color change ex: 'b--'

### Write here ###
x = np.linspace(0,50)
y = 8 * np.sinc(x)
plt.plot(x, y, 'b-.', label='something')
plt.title('Data')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.grid()
#plt.plot([2,4,6,8,10])
plt.show()

#--------------------------------------------------------------------------------------------------------

# Create a 3D plot of the same function as the previous problem
# Use the following to create the 3D plot:

# ax = plt.figure().add_subplot(projection='3d')
# ax.plot(x, y, zs=0, zdir='y')

# NOTE: x and y should be the x-axis and y-axis data from the previous problem

# For extra fun, make a for loop that will run in a range using linspace() and plot
# multiple sinc() functions in the xz plane at different values of y

### Write Here ###

ax = plt.figure().add_subplot(projection='3d')
ax.plot(x, y, zs=0, zdir='y')
'''for i in range(5):
    np.linspace(0,50)
    ax.plot(x, y, zs=0, zdir='y')
    plt.plot(x, y, 'b-.', label='something')
    No idea about this part'''
plt.show()



