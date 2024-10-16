# from glutInitialize import gluteSetup, displayPoints
from pyGameInitialize import pygameSetup
from Line.dda import ddaAlgo
from Line.bresenham import bresenham_line, bresenham_line_all_condition
from Circle.bresenham import bresenham_circle
from Circle.midpoint import midpoint_circle
from Two_dim_transformation.transformation import translation
from Two_dim_transformation.CohenSutherland import cohenSutherlandClip


def main():
    # ----inputs----
    # x1 = float(input('Give x1:'))
    # y1 = float(input('Give y1:'))
    # x2 = float(input('Give x2:'))
    # y2 = float(input('Give y2:'))
    # print(x1, y1, x2, y2)
    # start = [x1,y1]
    # end = [x2,y2]

    line_pixel = []
    # line_pixel = ddaAlgo([1, 10], [10, 10])
    # line_pixel = bresenham_line([0, 0], [10, 10])
    # line_pixel = bresenham_line_all_condition([1, 1], [-5, 10])
    # line_pixel = bresenham_circle(0, 0, 35)
    # line_pixel.append(midpoint_circle(0, 0, 5))
    # line_pixel = translation([[3, 7], [2, 3]], [25, -25])
    # cohenSutherlandClip(5, 5, 7, 7)
    # cohenSutherlandClip(7, 9, 11, 4)
    # cohenSutherlandClip(1, 5, 4, 1)

    line_pixel.append(bresenham_line_all_condition([1, 1], [-5, 10]))
    pygameSetup(line_pixel)


if __name__ == '__main__':
    main()
