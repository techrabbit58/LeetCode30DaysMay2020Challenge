"""
Week 1, Day 5: First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

    s = "leetcode"
    return 0.

    s = "loveleetcode",
    return 2.

N o t e

    You may assume the string contain only lowercase letters.

"""
import time
from collections import Counter


def firstUniqChar(s: str) -> int:
    """Stable runtime with O(n) complexity. Best average and worst case performance."""
    occurrences = Counter(s)
    for k, c in enumerate(s):
        if occurrences[c] == 1:
            return k
    return -1


def firstUniqChar_v2(s: str) -> int:
    """Fast if the first non-repeating char has a low index. Worst case complexity is O(n^2)."""
    already_seen = set()
    for k, c in enumerate(s):
        if c in already_seen:
            continue
        if s.count(c) == 1:
            return k
    return -1


def firstUniqChar_v3(s: str) -> int:
    """Slowest approach. Worst case complexity is O(n^2). Not much better than v2."""
    for k, c in enumerate(s):
        if s.find(c) == s.rfind(c):
            return k
    return -1


def firstUniqChar_v4(s: str) -> int:
    """Worst case complexity O(n^2), but good for some corner cases."""
    index = [s.index(c) for c in set(s) if s.count(c) == 1]
    return min(index) if index else -1


if __name__ == '__main__':

    print(firstUniqChar('leetcode'), 0)
    print(firstUniqChar('loveleetcode'), 2)
    print(firstUniqChar('abacabac'), -1)

    start = time.perf_counter_ns()
    print(firstUniqChar('the quick brown fox jumps over the lazy dog'), 4)
    print(firstUniqChar('bcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba'), 50)
    print(firstUniqChar('bcdefghijklmnopqrstuvwxyzbcdefghijklmnopqrstuvwxyza'), 50)
    print(firstUniqChar('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbxbbbbb'), 45)
    print('v1', time.perf_counter_ns() - start)

    start = time.perf_counter_ns()
    print(firstUniqChar_v2('the quick brown fox jumps over the lazy dog'), 4)
    print(firstUniqChar_v2('bcdefghijklmnopqrstuvwxyzbcdefghijklmnopqrstuvwxyza'), 50)
    print(firstUniqChar_v2('bcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba'), 50)
    print(firstUniqChar_v2('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbxbbbbb'), 45)
    print('v2', time.perf_counter_ns() - start)

    start = time.perf_counter_ns()
    print(firstUniqChar_v3('the quick brown fox jumps over the lazy dog'), 4)
    print(firstUniqChar_v3('bcdefghijklmnopqrstuvwxyzbcdefghijklmnopqrstuvwxyza'), 50)
    print(firstUniqChar_v3('bcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba'), 50)
    print(firstUniqChar_v3('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbxbbbbb'), 45)
    print('v3', time.perf_counter_ns() - start)

    start = time.perf_counter_ns()
    print(firstUniqChar_v4('the quick brown fox jumps over the lazy dog'), 4)
    print(firstUniqChar_v4('bcdefghijklmnopqrstuvwxyzbcdefghijklmnopqrstuvwxyza'), 50)
    print(firstUniqChar_v4('bcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba'), 50)
    print(firstUniqChar_v4('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbxbbbbb'), 45)
    print('v4', time.perf_counter_ns() - start)

# last line of code
