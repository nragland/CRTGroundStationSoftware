"""
Map Display

Uses live GPS data to track the LV and draws its path on the display.
"""

# (42.4517, -76.4912) (42.4430, -76.4746)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

data_path = 'testmapdata.csv'
data = pd.read_csv(data_path, names=['LATITUDE', 'LONGITUDE'], sep=',')

gps_data = tuple(zip(data['LATITUDE'].values, data['LONGITUDE'].values))

image = Image.open('map.png', 'r')
img_points = []

def scale_to_img(self, lat_lon, h_w):
    """
    From github
    """
    old = (self.points[2], self.points[0])
    new = (0, h_w[1])
    y = ((lat_lon[0] - old[0]) * (new[1] - new[0]) / (old[1] - old[0])) + new[0]
    old = (self.points[1], self.points[3])
    new = (0, h_w[0])
    x = ((lat_lon[1] - old[0]) * (new[1] - new[0]) / (old[1] - old[0])) + new[0]
    return int(x), h_w[1] - int(y)

for d in gps_data:
    x1, y1 = scale_to_img(d, (image.size[0], image.size[1]))  # Convert GPS coordinates to image coordinates.
    img_points.append((x1, y1))

draw = ImageDraw.Draw(image)
draw.line(img_points, fill=(255, 0, 0), width=2)  # Draw converted records to the map image.

image.save('resultMap.png')
