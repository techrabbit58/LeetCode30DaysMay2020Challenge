"""
Week 4, Day 5: Contiguous Array

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:

    Input: [0,1]
    Output: 2
    Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:

    Input: [0,1,0]
    Output: 2
    Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.
"""
from typing import List
from collections import defaultdict


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        index = defaultdict(list)
        balance = 0
        answer = 0
        for n, b in enumerate(nums):
            balance += 1 if b else -1
            index[balance].append(n + 1)
        print(index)
        return answer
            


if __name__ == '__main__':
    o = Solution()

    example = []
    expected = 0
    print(o.findMaxLength(example), expected)

    example = [0]
    expected = 0
    print(o.findMaxLength(example), expected)

    example = [1]
    expected = 0
    print(o.findMaxLength(example), expected)

    example = [0, 1]
    expected = 2
    print(o.findMaxLength(example), expected)

    example = [0, 1, 0]
    expected = 2
    print(o.findMaxLength(example), expected)

    example = [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]
    expected = 10
    print(o.findMaxLength(example), expected)

    example = [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1]
    expected = 10
    print(o.findMaxLength(example), expected)

    example = [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]
    expected = 4
    print(o.findMaxLength(example), expected)

    example = [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0]
    expected = 4
    print(o.findMaxLength(example), expected)

    example = [0, 1, 1, 0, 1, 1, 1, 0]
    expected = 4
    print(o.findMaxLength(example), expected)

# last line of code
