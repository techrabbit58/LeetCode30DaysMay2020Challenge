"""
Week 4, Day 7: Counting Bits

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num
calculate the number of 1's in their binary representation and return them as an array.

Example 1:

    Input: 2
    Output: [0,1,1]

Example 2:

    Input: 5
    Output: [0,1,1,2,1,2]

Follow up:

    It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can
    you do it in linear time O(n) /possibly in a single pass?

    Space complexity should be O(n).

    Can you do it like a boss? Do it without using any builtin function like __builtin_popcount
    in c++ or in any other language.

Hints:

    You should make use of what you have produced already.

    Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to generate new
    range from previous.

    Or does the odd/even status of the number help you in calculating the number of 1s?

"""
from typing import List
from functools import lru_cache


class Solution:
    def countBits(self, num: int) -> List[int]:
        @lru_cache(maxsize=None)
        def _count_one_bits(n: int) -> int:
            if n <= 1:
                return n
            return (n % 2) + _count_one_bits(n // 2)

        num = abs(num)
        answer = []
        for n in range(num + 1):
            answer.append(_count_one_bits(n))
        return answer


if __name__ == '__main__':
    o = Solution()

    num = 0
    expected = [0]
    print(o.countBits(num) == expected)

    num = 1
    expected = [0, 1]
    print(o.countBits(num) == expected)

    num = 2
    expected = [0, 1, 1]
    print(o.countBits(num) == expected)

    num = 3
    expected = [0, 1, 1, 2]
    print(o.countBits(num) == expected)

    num = 4
    expected = [0, 1, 1, 2, 1]
    print(o.countBits(num) == expected)

    num = 5
    expected = [0, 1, 1, 2, 1, 2]
    print(o.countBits(num) == expected)

# last line of code
