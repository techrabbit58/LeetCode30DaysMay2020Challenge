"""
Week 2, Day 4: Single Element in a Sorted Array

You are given a sorted array consisting of only integers where every
element appears exactly twice, except for one element which appears 
exactly once. Find this single element that appears only once.

Example 1:

    Input: [1,1,2,3,3,4,4,8,8]
    Output: 2

Example 2:

    Input: [3,3,7,7,10,11,11]
    Output: 10

Note: Your solution should run in O(log n) time and O(1) space.
"""
from typing import List


class Solution:
    """
    Solution complexities: time is O(n), space is O(1).
    The solution is fast, but worst case slower than O(log n).
    """

    def singleNonDuplicate(self, nums: List[int]) -> int:
        last_seen = None
        for num in nums:
            if last_seen is None:
                last_seen = num
            elif last_seen == num:
                last_seen = None
            else:
                break
        return last_seen


class SolutionV2:
    """
    Solution complexities: time is O(log n), space is O(1).
    """

    def singleNonDuplicate(self, nums: List[int]) -> int:
        j = 0
        k = len(nums) // 2
        while (k - j) > 1:
            if nums[k] == nums[k - 1]:
                j = k + 1
                k += (len(nums) - j) // 2
            else:
                k = (k - 1) // 2
        return nums[k]


if __name__ == '__main__':
    print(SolutionV2().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2)
    print(SolutionV2().singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]) == 10)
    print(SolutionV2().singleNonDuplicate([1]) == 1)
    print(SolutionV2().singleNonDuplicate([1, 1, 2]) == 2)

# last line of code
