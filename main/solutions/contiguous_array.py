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
from collections import defaultdict
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        (1) Preset the index for the zero offset string as -1 (means: the index before start)
        (2) For every index, calculate the (0, 1) balance. Indexes with equal balance must have
            an equal number of 0 and 1 between them.
        (3.1) If not balanced the given index so far, store it.
        (3.2) If already seen a given balance, the result must be the longest,
            or already seen, or this current substring. I.e. current index minus
            index when first seen this balance, if the max_length so far were not longer.
        :param nums: a list of 0 and 1, representing a bit stream
        :return: max possible length of substring with equal 1 and 0 bits
        """
        index = {0: -1}
        balance = max_length = 0
        for n, b in enumerate(nums):
            balance += b + b - 1
            if index.get(balance) is None:
                index[balance] = n
            else:
                max_length = max(max_length, n - index[balance])
        return max_length


if __name__ == '__main__':
    o = Solution()

    example = []
    expected = 0
    print(o.findMaxLength(example) == expected)

    example = [0]
    expected = 0
    print(o.findMaxLength(example) == expected)

    example = [1]
    expected = 0
    print(o.findMaxLength(example) == expected)

    example = [0, 1]
    expected = 2
    print(o.findMaxLength(example) == expected)

    example = [0, 1, 0]
    expected = 2
    print(o.findMaxLength(example) == expected)

    example = [0, 0, 1]
    expected = 2
    print(o.findMaxLength(example) == expected)

    example = [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]
    expected = 10
    print(o.findMaxLength(example) == expected)

    example = [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0]
    expected = 10
    print(o.findMaxLength(example) == expected)

    example = [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]
    expected = 4
    print(o.findMaxLength(example) == expected)

    example = [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0]
    expected = 4
    print(o.findMaxLength(example) == expected)

    example = [0, 1, 1, 0, 1, 1, 1, 0]
    expected = 4
    print(o.findMaxLength(example) == expected)

    example = [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0]
    expected = 6
    print(o.findMaxLength(example) == expected)

    example = [0, 0, 0, 0, 0]
    expected = 0
    print(o.findMaxLength(example) == expected)

    example = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    expected = 0
    print(o.findMaxLength(example) == expected)

    example = [0, 0, 0, 1, 0, 0, 0, 0]
    expected = 2
    print(o.findMaxLength(example) == expected)

    example = [1, 1, 1, 1, 1, 1, 0, 1, 1]
    expected = 2
    print(o.findMaxLength(example) == expected)

# last line of code
