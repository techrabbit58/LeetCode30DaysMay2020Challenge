"""
Week 1, Day 6: Majority Element

Given an array of size n, find the majority element. The majority element is the element that
appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

    Input: [3,2,3]
    Output: 3

Example 2:

    Input: [2,2,1,1,1,2,2]
    Output: 2

"""
from typing import List
from collections import Counter


def majorityElement(nums: List[int]) -> int:
    """This approach has complexity O(n)."""
    elements = Counter(nums)
    threshold = int(len(nums) / 2)
    for e, c in elements.items():
        if c > threshold:
            return e
    return 0


def majorityElement_v2(nums: List[int]) -> int:
    """This second approach is better, because less complex, has less dependencies, and runs quicker."""
    return list(sorted(nums))[int(len(nums) / 2)]


def majorityElement_v3(nums: List[int]) -> int:
    """
    Like v2, but it mutates the given nums array (i.e. sorts in place). Less space required,
    but we must accept a side effect (the mutated array.) Less operations, so it is
    supposed to be quicker then v2.
    """
    nums.sort()
    return nums[int(len(nums) / 2)]


def majorityElement_v4(nums: List[int]) -> int:
    """
    This solution relies on python magic, together with the idea that, if there is only one
    majority element, and there is always one, in any case, it must be the most common
    element in the given list. So we can let do Counter object the whole work.
    According to a post at LeetCode: https://leetcode.com/sapo96/
    """
    return Counter(nums).most_common()[0][0]


def majorityElement2(nums: List[int]) -> List[int]:
    """
    This solves a similar problem. It is LeetCode problem #229, Majority Element II:
    Find all elements in an array that appear more than ⌊ n/3 ⌋ times.
    """
    threshold = int(len(nums) / 3)
    counts = Counter(nums)
    return [k for k, v in counts.items() if v > threshold]


if __name__ == '__main__':

    print(majorityElement_v3([3, 2, 3]), 3)
    print(majorityElement_v3([2, 2, 1, 1, 1, 2, 2]), 2)

    print(majorityElement2([3, 2, 3]), [3])
    print(majorityElement2([1, 1, 1, 3, 3, 2, 2, 2]), [1, 2])

# last line of code
