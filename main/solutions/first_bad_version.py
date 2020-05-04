"""
Week 1, Day 1: First Bad Version

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of
your product fails the quality check. Since each version is developed based on the previous version, all the versions
after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following
ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to
find the first bad version. You should minimize the number of calls to the API.
"""
from typing import Callable


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
def API(bad_version: int) -> Callable[[int], bool]:
    def isBadVersion(version: int) -> bool:
        return bad_version <= version

    return isBadVersion


def firstBadVersion(n: int) -> int:
    low, mid, high = 0, int(n / 2), n
    while True:
        while isBadVersion(mid):
            high, mid = mid, low + max(1, (mid - low) // 2)
            if mid >= high:
                return high
        while not isBadVersion(mid):
            low, mid = mid, mid + max(1, (high - mid) // 2)
            if mid >= high:
                return high


def firstBadVersion_v2(n: int) -> int:
    left, right = 1, n
    while left < right:
        mid = int(left + (right - left) / 2)
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    bad_version = 4
    isBadVersion = API(bad_version)
    print(firstBadVersion_v2(5), bad_version)

# last line of code
