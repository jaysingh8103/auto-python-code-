# main.py (Unoptimized)
import math


def circle_area(radius):
    if radius < 0:
        return 0
    else:
        area = math.pi * radius**2
        print(f"Area is {area}")
        return area


circle_area(6)
