import numpy as np
points = []

def bresenham_line(start, end):
    # step 1 get end-points of line
    (x0, y0) = start
    (x1, y1) = end

    # step 2 calculate difference
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    m = dy / dx

    # step 3 perform test to check if pk < 0
    flag = True

    line_pixel = []
    line_pixel.append((x0, y0))

    step = 1
    if x0 > x1 or y0 > y1:
        step = -1

    mm = False
    if m < 1:
        x0, x1, y0, y1 = y0, y1, x0, x1
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        mm = True

    p0 = 2 * dx - dy
    x = x0
    y = y0

    for i in range(abs(y1 - y0)):
        if flag:
            x_previous = x0
            p_previous = p0
            p = p0
            flag = False
        else:
            x_previous = x
            p_previous = p

        if p >= 0:
            x = x + step

        p = p_previous + 2 * dx - 2 * dy * (abs(x - x_previous))
        y = y + 1

        if mm:
            line_pixel.append((y, x))
        else:
            line_pixel.append((x, y))

    line_pixel = np.array(line_pixel)

    return line_pixel


def draw_vertical_line(x_start, y_start, x_end, y_end):
    if y_start > y_end:
        temp = y_start
        y_start = y_end
        y_end = temp

    y = y_start
    while y <= y_end:
        points.append((x_start, y))
        y = y+1


def draw_horizontal_line(x_start, y_start, x_end, y_end):
    if x_start > x_end:
        temp = x_start
        x_start = x_end
        x_end = temp

    x = x_start
    while x <= x_end:
        print("looping ", x , x_end)
        points.append((x, y_start))
        x = x+1


def incremental_x(x_start, y_start, x_end, y_end, direction):
    x_start = x_start * direction
    x_end = x_end * direction

    if x_start > x_end:
        x_start, y_start, x_end, y_end = x_end, y_end, x_start, y_start

    dx = x_end - x_start
    dy = y_end - y_start
    d = 2*dy - dx
    dt = 2*(dy-dx)
    ds = 2*dy

    x, y = x_start, y_start

    while x < x_end:
        points.append((x * direction, y))
        x = x + 1
        if d < 0:
            d = d + ds
        else:
            y = y + 1
            d = d + dt
    points.append((x_end * direction, y_end))


def incremental_y(x_start, y_start, x_end, y_end, direction):
    y_start = y_start * direction
    y_end = y_end * direction

    if y_start > y_end:
        x_start, y_start, x_end, y_end = x_end, y_end, x_start, y_start

    dx = x_end - x_start
    dy = y_end - y_start
    d = 2*dx - dy
    dt = 2*(dx-dy)
    ds = 2*dx

    x, y = x_start, y_start

    while y < y_end:
        points.append((x, y * direction))
        y = y + 1
        if d < 0:
            d = d + ds
        else:
            x = x + 1
            d = d + dt
    points.append((x_end, y_end * direction))


def bresenham_line_all_condition(start, end):
    global points
    points = []

    x_start, y_start, x_end, y_end = start[0], start[1], end[0], end[1]

    dx = x_end - x_start
    dy = y_end - y_start

    if dx == 0:
        draw_vertical_line(x_start, y_start, x_end, y_end)
        return points
    elif dy == 0:
        draw_horizontal_line(x_start, y_start, x_end, y_end)
        return points

    m = dy/dx

    if 0 < m < 1:
        incremental_x(x_start, y_start, x_end, y_end, 1)
    elif m >= 1:
        incremental_y(x_start, y_start, x_end, y_end, 1)
    elif -1 < m < 0:
        incremental_x(x_start, y_start, x_end, y_end, -1)
    else:
        incremental_y(x_start, y_start, x_end, y_end, -1)
    return points

