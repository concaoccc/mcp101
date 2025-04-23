# area_of_circle.py
import math

def area_of_circle(radius):
    """Calculate the area of a circle given its radius."""
    return math.pi * radius ** 2

if __name__ == "__main__":
    r = float(input("Enter the radius of the circle: "))
    print(f"Area of the circle: {area_of_circle(r):.2f}")
