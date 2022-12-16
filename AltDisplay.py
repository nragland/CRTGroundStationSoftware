"""
Altimeter Display

Uses live altimeter data to track the LV and shows its path on the display.
"""

import csv
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time

# rocket speed: 800ft/sec

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
data = []
with open('testaltdata.csv') as csv_file:
    for row in csv.reader(csv_file):
        if row != []:
            data.append(row)

def animate(i, xs, ys):

    # Add x and y to lists
    if(data != []):
        xs.append(int(data[0][0]))
        ys.append(int(data[0][1]))
        del data[0]

        # Limit x and y lists to 20 items
        xs = xs[-20:]
        ys = ys[-20:]

        # Draw x and y lists
        ax.clear()
        ax.plot(xs, ys)

        # Format plot
        plt.title('Altitude vs Time')
        plt.ylabel('Alitude (ft)')
        ax.set_ylim([0, 12000])

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=200)
plt.show()
