from math import tan, pi


def polysum(n, s):
    """
    n: Number of sides of a regular polygon.
    s: Length of the sides of such polygon.
    This function returns the sum of the area and square of the perimeter of the regular polygon, rounded to 4 decimal places.
    """
    area = (0.25 * n * s**2)/(tan(pi/n))
    perimeter = s * n
    return round(area + perimeter**2, 4)
