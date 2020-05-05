"""
Week 1, Day 5
First Unique Character in a String

Given a string, find the first non-repeating 
character in it and return it's index. 

If it doesn't exist, return -1.

Examples:

    s = "leetcode"
    return 0.

    s = "loveleetcode",
    return 2.

N o t e

    You may assume the string contain only
    lowercase letters.
"""
from collections import Counter


def firstUniqChar(s: str) -> int:
    occurrences = Counter(s)
    for k, c in enumerate(s):
        if occurrences[c] == 1:
            return k
    return -1


if __name__ == '__main__':
    print(firstUniqChar('leetcode'), 0)
    print(firstUniqChar('loveleetcode'), 2)
    print(firstUniqChar('abacabac'), -1)

# last line of code
