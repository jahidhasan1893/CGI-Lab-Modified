from pyGameInitialize import pygameSetup  # Import pygame setup module
from Line.dda import ddaAlgo  # Import DDA line drawing algorithm
from Line.bresenham import bresenham_line, bresenham_line_all_condition  # Import Bresenham line algorithms
from Circle.bresenham import bresenham_circle  # Import Bresenham circle algorithm
from Circle.midpoint import midpoint_circle  # Import Midpoint circle algorithm
from Two_dim_transformation.transformation import translation, rotation, reflection, scaling, shearing  # Import 2D transformations
from Two_dim_transformation.CohenSutherland import cohenSutherlandClip  # Import line clipping algorithm


def main():
    line_pixel = []
    
    while True:
        print("\nComputer Graphics Operations Menu:")
        print("1. Draw line using DDA algorithm")
        print("2. Draw line using basic Bresenham algorithm")
        print("3. Draw line using Bresenham for all conditions")
        print("4. Draw circle using Bresenham algorithm")
        print("5. Draw circle using Midpoint algorithm")
        print("6. Perform 2D translation")
        print("7. Perform 2D rotation")
        print("8. Perform 2D reflection")
        print("9. Perform 2D scaling")
        print("10. Perform 2D shearing")
        print("11. Perform line clipping")
        print("12. Draw Rectangle")
        print("13. Draw Triangle")
        print("14. Draw Square")
        print("15. Draw Pentagon")
        print("16. Clear Screen")
        print("17. Undo Last Operation")
        print("18. Draw Shaheed Minar")
        print("19. Type 'SUST'")
        print("20. Exit")
        
        choice = input("\nEnter your choice (1-20): ")
        
        if choice == '1':
            x1 = int(input('Enter x1: '))
            y1 = int(input('Enter y1: '))
            x2 = int(input('Enter x2: '))
            y2 = int(input('Enter y2: '))
            line_pixel.append(ddaAlgo([x1, y1], [x2, y2]))
            
        elif choice == '2':
            x1 = int(input('Enter x1: '))
            y1 = int(input('Enter y1: '))
            x2 = int(input('Enter x2: '))
            y2 = int(input('Enter y2: '))
            line_pixel.append(bresenham_line([x1, y1], [x2, y2]))
            
        elif choice == '3':
            x1 = int(input('Enter x1: '))
            y1 = int(input('Enter y1: '))
            x2 = int(input('Enter x2: '))
            y2 = int(input('Enter y2: '))
            line_pixel.append(bresenham_line_all_condition([x1, y1], [x2, y2]))
            
        elif choice == '4':
            x = int(input('Enter center x: '))
            y = int(input('Enter center y: '))
            r = int(input('Enter radius: '))
            line_pixel.append(bresenham_circle(x, y, r))
            
        elif choice == '5':
            x = int(input('Enter center x: '))
            y = int(input('Enter center y: '))
            r = int(input('Enter radius: '))
            line_pixel.append(midpoint_circle(x, y, r))
            
        elif choice == '6':
            x1 = float(input('Enter point1 x: '))
            y1 = float(input('Enter point1 y: '))
            x2 = float(input('Enter point2 x: '))
            y2 = float(input('Enter point2 y: '))
            tx = float(input('Enter translation in x: '))
            ty = float(input('Enter translation in y: '))
            line_pixel.append(translation([[x1, y1], [x2, y2]], [tx, ty]))
            
        elif choice == '7':
            x1 = float(input('Enter point1 x: '))
            y1 = float(input('Enter point1 y: '))
            x2 = float(input('Enter point2 x: '))
            y2 = float(input('Enter point2 y: '))
            angle = float(input('Enter rotation angle (in degrees): '))
            line_pixel.append(rotation([[x1, y1], [x2, y2]], angle))
            
        elif choice == '8':
            x1 = float(input('Enter point1 x: '))
            y1 = float(input('Enter point1 y: '))
            x2 = float(input('Enter point2 x: '))
            y2 = float(input('Enter point2 y: '))
            axis = input('Enter reflection axis (x/y): ')
            line_pixel.append(reflection([[x1, y1], [x2, y2]], axis))
            
        elif choice == '9':
            x1 = float(input('Enter point1 x: '))
            y1 = float(input('Enter point1 y: '))
            x2 = float(input('Enter point2 x: '))
            y2 = float(input('Enter point2 y: '))
            sx = float(input('Enter scaling factor for x: '))
            sy = float(input('Enter scaling factor for y: '))
            line_pixel.append(scaling([[x1, y1], [x2, y2]], sx, sy))
            
        elif choice == '10':
            x1 = float(input('Enter point1 x: '))
            y1 = float(input('Enter point1 y: '))
            x2 = float(input('Enter point2 x: '))
            y2 = float(input('Enter point2 y: '))
            shx = float(input('Enter shearing factor for x: '))
            shy = float(input('Enter shearing factor for y: '))
            line_pixel.append(shearing([[x1, y1], [x2, y2]], shx, shy))
            
        elif choice == '11':
            x1 = float(input('Enter x1: '))
            y1 = float(input('Enter y1: '))
            x2 = float(input('Enter x2: '))
            y2 = float(input('Enter y2: '))
            cohenSutherlandClip(x1, y1, x2, y2)
            
        elif choice == '12':
            x = int(input('Enter top-left x: '))
            y = int(input('Enter top-left y: '))
            width = int(input('Enter width: '))
            height = int(input('Enter height: '))
            line_pixel.append(bresenham_line_all_condition([x, y], [x + width, y]))
            line_pixel.append(bresenham_line_all_condition([x + width, y], [x + width, y + height]))
            line_pixel.append(bresenham_line_all_condition([x + width, y + height], [x, y + height]))
            line_pixel.append(bresenham_line_all_condition([x, y + height], [x, y]))
            
        elif choice == '13':
            x1 = int(input('Enter x1: '))
            y1 = int(input('Enter y1: '))
            x2 = int(input('Enter x2: '))
            y2 = int(input('Enter y2: '))
            x3 = int(input('Enter x3: '))
            y3 = int(input('Enter y3: '))
            line_pixel.append(bresenham_line_all_condition([x1, y1], [x2, y2]))
            line_pixel.append(bresenham_line_all_condition([x2, y2], [x3, y3]))
            line_pixel.append(bresenham_line_all_condition([x3, y3], [x1, y1]))
            
        elif choice == '14':
            x = int(input('Enter top-left x: '))
            y = int(input('Enter top-left y: '))
            size = int(input('Enter size: '))
            line_pixel.append(bresenham_line_all_condition([x, y], [x + size, y]))
            line_pixel.append(bresenham_line_all_condition([x + size, y], [x + size, y + size]))
            line_pixel.append(bresenham_line_all_condition([x + size, y + size], [x, y + size]))
            line_pixel.append(bresenham_line_all_condition([x, y + size], [x, y]))
            
        elif choice == '15':
            x = int(input('Enter center x: '))
            y = int(input('Enter center y: '))
            radius = int(input('Enter radius: '))
            from math import cos, sin, pi
            vertices = []
            for i in range(5):
                angle = 2 * pi * i / 5 - pi / 2
                vx = x + radius * cos(angle)
                vy = y + radius * sin(angle)
                vertices.append([int(vx), int(vy)])
            for i in range(5):
                line_pixel.append(bresenham_line_all_condition(vertices[i], vertices[(i + 1) % 5]))
            
        elif choice == '16':
            line_pixel.clear()
            
        elif choice == '17':
            if line_pixel:
                line_pixel.pop()

        elif choice == '18':
            line_pixel.append(midpoint_circle(0, 0, 5))
            
            # Left section
            line_pixel.append(bresenham_line_all_condition([-30, -20], [-30, 15]))
            line_pixel.append(bresenham_line_all_condition([-30, 15], [-20, 15]))
            line_pixel.append(bresenham_line_all_condition([-20, -20], [-20, 15]))
            
            # Center section
            line_pixel.append(bresenham_line_all_condition([-10, -20], [-10, 15]))
            line_pixel.append(bresenham_line_all_condition([-10, 15], [0, 25]))
            line_pixel.append(bresenham_line_all_condition([0, 15], [10, 25]))
            line_pixel.append(bresenham_line_all_condition([10, 15], [20, 25]))
            line_pixel.append(bresenham_line_all_condition([0, 25], [20, 25]))
            line_pixel.append(bresenham_line_all_condition([0, 5], [0, 15]))
            line_pixel.append(bresenham_line_all_condition([0, -5], [0, -20]))
            line_pixel.append(bresenham_line_all_condition([10, -20], [10, 15]))
            
            # Right section
            line_pixel.append(bresenham_line_all_condition([20, -20], [20, 15]))
            line_pixel.append(bresenham_line_all_condition([20, 15], [30, 15]))
            line_pixel.append(bresenham_line_all_condition([30, -20], [30, 15]))
            
            # Base section
            line_pixel.append(bresenham_line_all_condition([-45, -20], [45, -20]))
            line_pixel.append(bresenham_line_all_condition([-45, -20], [-40, -25]))
            line_pixel.append(bresenham_line_all_condition([-40, -25], [-35, -30]))
            line_pixel.append(bresenham_line_all_condition([45, -20], [40, -25]))
            line_pixel.append(bresenham_line_all_condition([40, -25], [35, -30]))
            line_pixel.append(bresenham_line_all_condition([-40, -25], [40, -25]))
            line_pixel.append(bresenham_line_all_condition([-35, -30], [35, -30]))

        elif choice == '19':
            # Letter S
            line_pixel.append([(-45, 0, -35, 15)])
            line_pixel.append([(-45, 0, -35, 0, 1)])
            line_pixel.append([(-45, -15, -35, 0)])
            
            # Letter U
            line_pixel.append([(-25, 15, -25, -15)])
            line_pixel.append([(-25, -15, -10, -15)])
            line_pixel.append([(-10, -15, -10, 15)])
            
            # Letter S
            line_pixel.append([(0, 15, 10, 15)])
            line_pixel.append([(0, 15, 0, 0)])
            line_pixel.append([(0, 0, 10, 0)])
            line_pixel.append([(10, 0, 10, -15)])
            line_pixel.append([(0, -15, 10, -15)])
            
            # Letter T
            line_pixel.append([(20, 15, 40, 15, 1)])
            line_pixel.append([(30, 15, 30, -15, 1)])
            
        elif choice == '20':
            break
            
        else:
            print("Invalid choice! Please try again.")
            continue
        
        pygameSetup(line_pixel)


if __name__ == '__main__':
    main()