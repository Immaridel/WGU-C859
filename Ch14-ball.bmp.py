"""
https://zytools.zybooks.com/zyAuthor/Python/IMAGES/ball.bmp
"""

import struct

ball_file = open('ball.bmp', 'rb')
ball_data = ball_file.read()
ball_file.close()

# BMP image file format stores location
# of pixel RGB values in bytes 10-14
pixel_data_loc = ball_data[10:14]

# Converts byte sequence into integer object
pixel_data_loc = struct.unpack('<L', pixel_data_loc)[0]

# Create sequence of 3000 red, green, and yellow pixels each
new_pixels = b'\x01'*3000 + b'\x02'*3000 + b'\x03'*3000

# Overwrite pixels in image with new pixels
new_ball_data = ball_data[:pixel_data_loc] + \
              new_pixels + \
              ball_data[pixel_data_loc + len(new_pixels):]

# Write new image
new_ball_file = open('new_ball.bmp', 'wb')
new_ball_file.write(new_ball_data)
new_ball_file.close()