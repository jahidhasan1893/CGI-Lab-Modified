points = []


def eight_way_symmetric_plot(xc, yc, x, y):
    points.append((x + xc, y + yc))
    points.append((x + xc, -y + yc))
    points.append((-x + xc, -y + yc))
    points.append((-x + xc, y + yc))
    points.append((y + xc, x + yc))
    points.append((y + xc, -x + yc))
    points.append((-y + xc, -x + yc))
    points.append((-y + xc, x + yc))


def bresenham_circle(xc=200, yc=200, r=100):
    x = 0
    y = r
    d = 3 - (2 * r)
    eight_way_symmetric_plot(xc, yc, x, y)

    while x <= y:
        if d <= 0:
            d = d + (4 * x) + 6
        else:
            d = d + (4 * x) - (4 * y) + 10
            y = y - 1
        x = x + 1
        eight_way_symmetric_plot(xc, yc, x, y)
    return points
