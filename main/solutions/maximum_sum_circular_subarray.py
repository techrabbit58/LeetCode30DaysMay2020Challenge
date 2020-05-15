"""
Week 3, Day 1: Maximum Sum Circular Subarray

Given a circular array C of integers represented by A, find the maximum
possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the 
beginning of the array. (Formally, C[i] = A[i] when 0 <= i < A.length,
and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at
most once. (Formally, for a subarray C[i], C[i+1], ..., C[j], there does 
not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

E x a m p l e s

    Input: [1,-2,3,-2]
    Output: 3
    Explanation: Subarray [3] has maximum sum 3

    Input: [5,-3,5]
    Output: 10
    Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10

    Input: [3,-1,2,-1]
    Output: 4
    Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4

    Input: [3,-2,2,-3]
    Output: 3
    Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3

    Input: [-2,-3,-1]
    Output: -1
    Explanation: Subarray [-1] has maximum sum -1

N o t e s

    (1) -30000 <= A[i] <= 30000
    (2) 1 <= A.length <= 30000

H i n t s

For those of you who are familiar with the Kadane's algorithm, think in
terms of that. For the newbies, Kadane's algorithm is used to finding 
the maximum sum subarray from a given array. This problem is a twist on
that idea.

The subarray we are looking for, can be in the middle of the simple array,
or can be split across the ends, if we take it as a circular subarray.
"""
from typing import List, Tuple
from itertools import islice


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        def max_subarray_sum(arr: List[int]) -> int:
            current_sum = max_sum = arr[0]
            for n in arr[1:]:
                current_sum = n + max(0, current_sum)
                max_sum = max(current_sum, max_sum)
            return max_sum

        subarray_sum = max_subarray_sum(A)
        circular_sum = sum(A) + max_subarray_sum([-n for n in A])
        return circular_sum if circular_sum > subarray_sum and circular_sum != 0 else subarray_sum


class SolutionV2:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        def complementary_kadane(arr):
            current_sum = max_sum = num_sum = arr[0]
            current_complement = complement = -arr[0]
            for n in islice(arr, 1, None):
                current_sum = max(n, current_sum + n)
                current_complement = max(-n, current_complement - n)
                max_sum = max(current_sum, max_sum)
                complement = max(complement, current_complement)
                num_sum += n
            return max_sum, complement, num_sum

        subarray_sum, complement, array_sum = complementary_kadane(A)
        circular_sum = array_sum + complement
        return circular_sum if circular_sum > subarray_sum and circular_sum != 0 else subarray_sum


if __name__ == '__main__':

    obj = Solution()

    print(obj.maxSubarraySumCircular([1, -2, 3, -2]) == 3)
    print(obj.maxSubarraySumCircular([5, -3, 5]) == 10)
    print(obj.maxSubarraySumCircular([3, -1, 2, -1]) == 4)
    print(obj.maxSubarraySumCircular([3, -2, 2, -3]) == 3)
    print(obj.maxSubarraySumCircular([-2, -3, -1]) == -1)

# last line of code
