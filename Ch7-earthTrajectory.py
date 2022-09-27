import math
'''
Use inputs to test:
45
100
3
'''


def trajectory(t, a, v, g, h):
    """Calculates new x,y position"""
    x = v * t * math.cos(a)
    y = h + v * t * math.sin(a) - 0.5 * g * t * t
    return (x, y)


def degree_to_radians(degrees):
    """Converts degrees to radians"""
    return ((degrees * math.pi) / 180.0)

if __name__ == '__main__':
    gravity = 9.81  # Earth gravity (m/s^2)
    time = 1.0  # time (s)
    x_loc = 0
    h = 0

    angle = float(input('Launch angle (deg): '))
    print(angle)
    angle = degree_to_radians(angle)

    velocity = float(input('Launch velocity (m/s): '))
    print(velocity)

    height = float(input('Initial height (m): '))
    y_loc = height
    print(y_loc)

    while (y_loc >= 0.0):  # While above ground
        print('Time {:3.0f} x = {:3.0f} y = {:3.0f}'.format(time, x_loc, y_loc))
        x_loc, y_loc = trajectory(time, angle, velocity, gravity, height)
        time += 1.0
