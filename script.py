# Import necessary modules
from copy import copy
import math

# Class definitions with attributes
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, x, y, width, height):
        self.corner = Point(x, y)
        self.width = width
        self.height = height


class Circle:
    def __init__(self, x, y, r):
        self.center = Point(x, y)
        self.radius = r


# Function definitions
def distance_between_points(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    return math.sqrt(dx ** 2 + dy ** 2)


def point_in_circle(point, circle):
    return distance_between_points(point, circle.center) <= circle.radius


def rect_in_circle(rect, circle):
    p = copy(rect.corner)
    if not point_in_circle(p, circle):
        return False

    p.x += rect.width
    if not point_in_circle(p, circle):
        return False

    p.y -= rect.height
    if not point_in_circle(p, circle):
        return False

    p.x -= rect.width
    if not point_in_circle(p, circle):
        return False

    return True


def rect_circle_overlap(rect, circle):
    p = copy(rect.corner)
    if point_in_circle(p, circle):
        return True

    p.x += rect.width
    if point_in_circle(p, circle):
        return True

    p.y -= rect.height
    if point_in_circle(p, circle):
        return True

    p.x -= rect.width
    if point_in_circle(p, circle):
        return True

    return False


# Creating class objects with instance attributes
point = Point(50, 50)
box = Rectangle(50, 50, 100, 200)
circle = Circle(150, 100, 75)

# Printing out the results
print(point_in_circle(point, circle))
print(rect_in_circle(box, circle))
print(rect_circle_overlap(box, circle))
