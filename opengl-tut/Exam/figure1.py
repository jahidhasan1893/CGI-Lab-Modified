from pyGameInitialize import pygameSetup
# from Line.dda import ddaAlgo
from Line.bresenham import bresenham_line, bresenham_line_all_condition
# from Circle.bresenham import bresenham_circle
from Circle.midpoint import midpoint_circle
# from Two_dim_transformation.transformation import translation
# from Two_dim_transformation.CohenSutherland import cohenSutherlandClip


def main():
    line_pixel = []
    # line_pixel = ddaAlgo([1, 10], [10, 10])
    # line_pixel = bresenham_line([0, 0], [10, 10])
    # line_pixel = bresenham_line_all_condition([1, 1], [-5, 10])
    # line_pixel = bresenham_circle(0, 0, 35)
    line_pixel.append(midpoint_circle(0, 0, 5))
    # line_pixel = translation([[3, 7], [2, 3]], [25, -25])
    # cohenSutherlandClip(5, 5, 7, 7)
    # cohenSutherlandClip(7, 9, 11, 4)
    # cohenSutherlandClip(1, 5, 4, 1)



    # ------left-------
    # left-leftmost
    line_pixel.append(bresenham_line_all_condition([-30, -20], [-30, 15]))
    # left-topmost
    line_pixel.append(bresenham_line_all_condition([-30, 15], [-20, 15]))
    # left-rightmost
    line_pixel.append(bresenham_line_all_condition([-20, -20], [-20, 15]))



    # -------center--------
    # center-left-line
    line_pixel.append(bresenham_line_all_condition([-10, -20], [-10, 15]))

    # ---- center-line ----
    # center-top-angel-left
    line_pixel.append(bresenham_line_all_condition([-10, 15], [0, 25]))
    # center-top-angel-middle
    line_pixel.append(bresenham_line_all_condition([0, 15], [10, 25]))
    # center-top-angel-right
    line_pixel.append(bresenham_line_all_condition([10, 15], [20, 25]))

    # center-top-angel-top
    line_pixel.append(bresenham_line_all_condition([0, 25], [20, 25]))
    # # center-top-angel-top-rightmost
    # line_pixel.append(bresenham_line_all_condition([10, 15], [20, 25]))


    # center-top-half
    line_pixel.append(bresenham_line_all_condition([0, 5], [0, 15]))
    # center-bottom-half
    line_pixel.append(bresenham_line_all_condition([0, -5], [0, -20]))

    # center-right-line
    line_pixel.append(bresenham_line_all_condition([10, -20], [10, 15]))



    # ------right-------
    # right-leftmost
    line_pixel.append(bresenham_line_all_condition([20, -20], [20, 15]))
    # right-topmost
    line_pixel.append(bresenham_line_all_condition([20, 15], [30, 15]))
    # right-rightmost
    line_pixel.append(bresenham_line_all_condition([30, -20], [30, 15]))

    # -------base---------
    # base-top-straight
    line_pixel.append(bresenham_line_all_condition([-45, -20], [45, -20]))

    # base-top-to-middle-left
    line_pixel.append(bresenham_line_all_condition([-45, -20], [-40, -25]))
    # base-middle-to-bottom-left
    line_pixel.append(bresenham_line_all_condition([-40, -25], [-35, -30]))


    # base-top-to-middle-right
    line_pixel.append(bresenham_line_all_condition([45, -20], [40, -25]))
    # base-middle-to-bottom-right
    line_pixel.append(bresenham_line_all_condition([40, -25], [35, -30]))

    # base-middle-straight
    line_pixel.append(bresenham_line_all_condition([-40, -25], [40, -25]))

    # base-bottom-straight
    line_pixel.append(bresenham_line_all_condition([-35, -30], [35, -30]))





    pygameSetup(line_pixel)


if __name__ == '__main__':
    main()