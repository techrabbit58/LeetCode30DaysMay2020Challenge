"""
Week 5, Day 2: K Closest Points to Origin

We have a list of points on the plane. Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in.)

Example 1:

    Input: points = [[1,3],[-2,2]], K = 1
    Output: [[-2,2]]
    Explanation:
        The distance between (1, 3) and the origin is sqrt(10).
        The distance between (-2, 2) and the origin is sqrt(8).
        Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
        We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

    Input: points = [[3,3],[5,-1],[-2,4]], K = 2
    Output: [[3,3],[-2,4]]

    (The answer [[-2,4],[3,3]] would also be accepted.)

Note:

    1 <= K <= points.length <= 10000
    -10000 < points[i][0] < 10000
    -10000 < points[i][1] < 10000

"""
import json
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)[:K]


def equals(A: List[List[int]], B: List[List[int]]) -> bool:
    set_a = set((a, b) for a, b in A)
    set_b = set((a, b) for a, b in B)
    return set_a == set_b


if __name__ == '__main__':
    o = Solution()

    points = [[1, 3], [-2, 2]]
    K = 1
    expected = [[-2, 2]]
    print(equals(o.kClosest(points, K), expected))

    points = [[3, 3], [5, -1], [-2, 4]]
    K = 2
    expected = [[3, 3], [-2, 4]]
    print(equals(o.kClosest(points, K), expected))

    points = [[3, 3], [5, -1], [2, 4], [-2, 4]]
    K = 2
    expected = [[3, 3], [2, 4]]
    print(equals(o.kClosest(points, K), expected))

    points = [[0, 1], [1, 0]]
    K = 2
    expected = [[0, 1], [1, 0]]
    print(equals(o.kClosest(points, K), expected))

    points = [[1, 3], [-2, 2], [2, -2]]
    K = 2
    expected = [[-2, 2], [2, -2]]
    print(equals(o.kClosest(points, K), expected))

    points = json.load(open('points.json'))
    K = 5313
    expected = json.load(open('points_expected.json'))
    print(equals(o.kClosest(points, K), expected))

# last line of code
