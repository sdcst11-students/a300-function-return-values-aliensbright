#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math

def distance(a,b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    answer = (x**2+y**2)**0.5
    return answer

if __name__ == "__main__":
    d = distance((2,4),(6,3))
    assert round(d,3) == 4.123
    d = distance( (-3,2.2) , (1,2))
    assert round(d,3) == 4.005


