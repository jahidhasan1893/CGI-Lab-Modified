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


def midpoint_circle(xc=0, yc=0, r=0):
    x = 0
    y = r
    p = 1 - r

    while x <= y:
        eight_way_symmetric_plot(xc, yc, x, y)
        x = x + 1
        if p < 0:
            p = p + (2 * x) + 1
        else:
            p = p + 2 * (x - y) + 1
            y = y - 1
    return points
