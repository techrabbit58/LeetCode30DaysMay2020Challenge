"""
Week 4, Day 2: Interval List Intersections

Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The
intersection of two closed intervals is a set of real numbers that is either empty, or can be represented
as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

Note 1:

    0 <= A.length < 1000
    0 <= B.length < 1000
    0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9

"""
from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        a, b, LA, LB, result = 0, 0, len(A), len(B), []
        while a < LA and b < LB:
            first_of_a, last_of_a, first_of_b, last_of_b = A[a], B[b]
            first_of_overlap, last_of_overlap = max(first_of_a, first_of_b), min(last_of_a, last_of_b)
            if first_of_overlap <= last_of_overlap:
                result.append([first_of_overlap, last_of_overlap])
            if last_of_a <= last_of_b:
                a += 1
            else:
                b += 1
        return result


if __name__ == '__main__':
    o = Solution()

    A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B = [[1, 5], [8, 12], [15, 24], [25, 26]]
    expected = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
    print('A =', A, '\nB =', B, '\noutput   =', o.intervalIntersection(A, B), '\nexpected =', expected, '\n')

# last line of code
