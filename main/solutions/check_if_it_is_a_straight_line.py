"""
Seek 2, Day 1: Check If It Is a Straight Line

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents
the coordinate of a point. Check if these points make a straight line in the XY plane.

C o n s t r a i n t s

    2 <= coordinates.length <= 1000
    coordinates[i].length == 2
    -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
    coordinates contains no duplicate point.

H i n t s

    If there're only 2 points, return true.
    Check if all other points lie on the line defined by the first 2 points.
    Use cross product to check collinearity.

"""
from typing import List
from itertools import islice


def checkStraightLine(coordinates: List[List[int]]) -> bool:
    """
    This solution runs memory efficient and relatively fast.
    Execution: O(n), Memory: O(1).
    """
    if len(coordinates) == 2:
        return True
    (x0, y0), (x1, y1) = coordinates[:2]
    dx, dy = x0 - x1, y0 - y1
    for pn in islice(coordinates, 2, None):
        if (dy * (x0 - pn[0]) - dx * (y0 - pn[1])):
            return False
    return True


if __name__ == '__main__':
    print(checkStraightLine([[-3, 2], [2, 3]]) is True)
    print(checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) is True)
    print(checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]) is False)
    print(checkStraightLine([[1, 1], [2, 2], [3, 1], [4, 2], [5, 3], [7, 5]]) is False)

# last line of code
