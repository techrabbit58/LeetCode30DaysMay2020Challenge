"""
Week 4, Day 4: Uncrossed Lines

We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

    A[i] == B[j];

The line we draw does not intersect any other connecting (non-horizontal) line. Note that a connecting
lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.

Example 1:

    Input: A = [1,4,2], B = [1,2,4]
    Output: 2
    Explanation: We can draw 2 uncrossed lines as in the diagram. We cannot draw 3 uncrossed lines,
    because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.

Example 2:

    Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
    Output: 3

Example 3:

    Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
    Output: 2

Notes:

    1 <= A.length <= 500
    1 <= B.length <= 500
    1 <= A[i], B[i] <= 2000

Hint:

    Think dynamic programming. Given an oracle dp(i,j) that tells us how many lines A[i:], B[j:]
    [the sequence A[i], A[i+1], ... and B[j], B[j+1], ...] are uncrossed, can we write this as
    a recursion?

Remark:

    The given solution comes from
    https://massivealgorithms.blogspot.com/2019/06/leetcode-1035-uncrossed-lines.html

"""
from typing import List


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        LA, LB = len(A), len(B)
        dp = [[0] * (LA + 1) for _ in range(LB + 1)]
        for x, a in enumerate(A):
            for y, b in enumerate(B):
                if a == b:
                    dp[y + 1][x + 1] = 1 + dp[y][x]
                else:
                    dp[y + 1][x + 1] = max(dp[y + 1][x], dp[y][x + 1])
        return dp[LB][LA]


if __name__ == '__main__':

    o = Solution()

    A = [1, 4, 2]
    B = [1, 2, 4]
    expected = 2
    print(o.maxUncrossedLines(A, B) == expected)

    A = [2, 5, 1, 2, 5]
    B = [10, 5, 2, 1, 5, 2]
    expected = 3
    print(o.maxUncrossedLines(A, B) == expected)

    A = [1, 3, 7, 1, 7, 5]
    B = [1, 9, 2, 5, 1]
    expected = 2
    print(o.maxUncrossedLines(A, B) == expected)

# last line of code
