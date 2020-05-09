"""
Week 2, Day 2: Valid Perfect Square

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note:
    
    Do not use any built-in library function such as sqrt.

Example 1:

    Input: 16
    Output: true

Example 2:

    Input: 14
    Output: false

"""
from functools import reduce
from time import perf_counter_ns


def isPerfectSquare(num: int) -> bool:
    """Okay. Solution is O(1)."""
    r = int(num ** 0.5)
    return r * r == num


def isPerfectSquare_v2(num: int) -> bool:
    """
    This O(1) solution were contributed to LeetCode by another user.
    Way faster than my first solution!
    A good example why you should always: 'Know your standard API!'
    But there is so much much python magic in it, that it almost feels like cheating.
    """
    return (num ** 0.5).is_integer()


def isPerfectSquare_v3(num: int) -> bool:
    """
    Solve with math. Because (x + 1)^2 = x^2 + 2*x + 1. With 2*x + 1 being an odd number.
    This math based solution is O(n), and not O(1), so it is elegant, but slow.
    """
    x = 1
    while num > 0:
        num -= x
        x += 2
    return num == 0


if __name__ == '__main__':

    p = 4321 * 4321
    q = 4321 * 4319

    start = perf_counter_ns()
    print(isPerfectSquare(16) is True)
    print(isPerfectSquare(14) is False)
    print(isPerfectSquare(p) is True)
    print(isPerfectSquare(q) is False)
    print('v1', perf_counter_ns() - start)

    start = perf_counter_ns()
    print(isPerfectSquare_v2(16) is True)
    print(isPerfectSquare_v2(14) is False)
    print(isPerfectSquare_v2(p) is True)
    print(isPerfectSquare_v2(q) is False)
    print('v2', perf_counter_ns() - start)

    start = perf_counter_ns()
    print(isPerfectSquare_v3(16) is True)
    print(isPerfectSquare_v3(14) is False)
    print(isPerfectSquare_v3(p) is True)
    print(isPerfectSquare_v3(q) is False)
    print('v3', perf_counter_ns() - start)

# last line of code
