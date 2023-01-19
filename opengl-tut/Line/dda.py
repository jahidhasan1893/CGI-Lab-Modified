import math

def ddaAlgo(start, end):
    line_pixels = []
    if start[0] > end[0]:
        start, end = end, start
    (x1, y1) = start
    (x2, y2) = end
    y_final = y1
    x_final = x1
    if x1 == x2:
        if y1 > y2:
            start, end = end, start
            (x1, y1) = start
            (x2, y2) = end
            x_final = x1
        m_inv = 0
        while y1 <= y2:
            x = math.floor(x_final+0.5)
            line_pixels.append((x, y1))
            y1 = y1+1
            x_final = x_final + m_inv
        return line_pixels
    m = (y2 - y1) / (x2 - x1)
    line_pixels.append((x1, y1))

    if abs(m) <= 1:
        while x1 <= x2:
            y = math.floor(y_final+0.5)
            line_pixels.append((x1, y))
            x1 = x1+1
            y_final = y_final + m
    else:
        m_inv = 1/m
        if y1 > y2:
            start, end = end, start
            (x1, y1) = start
            (x2, y2) = end
            x_final = x1

        while y1 <= y2:
            x = math.floor(x_final+0.5)
            line_pixels.append((x, y1))
            y1 = y1+1
            x_final = x_final + m_inv
    return line_pixels
