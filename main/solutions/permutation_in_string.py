"""
Week 3, Day 4: Permutation in String

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
In other words, one of the first string's permutations is the substring of the second string.

Example 1:

    Input: s1 = "ab" s2 = "eidbaooo"
    Output: True
    Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

    Input:s1= "ab" s2 = "eidboaoo"
    Output: False


N o t e s

    The input strings only contain lower case letters.
    The length of both given strings is in range [1, 10,000].

H i n t s

(1) Obviously, brute force will result in 'Time Limit Exceeded' (TLE). Think of something else.
(2) How will you check whether one string is a permutation of another string?
(3) One way is to sort the string and then compare. But, Is there a better way?
(4) If one string is a permutation of another string then they must one common metric. What is that?
(5) Both strings must have same character frequencies, if one is permutation of another.
    Which data structure should be used to store frequencies?
(6) What about hash table? An array of size 26?

"""
from itertools import islice


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1 > len_s2:
            return False
        s1_hash = sum(hash(ch) for ch in s1)
        s2_hash = sum(hash(s2[k]) for k in range(len_s1))
        if s1_hash == s2_hash:
            return True
        for k in range(len_s1, len_s2):
            s2_hash += hash(s2[k]) - hash(s2[k - len_s1])
            if s1_hash == s2_hash:
                return True
        return False


if __name__ == '__main__':
    obj = Solution()

    s1, s2, expected = 'ab', 'eidbaooo', True
    print(obj.checkInclusion(s1, s2) == expected)

    s1, s2, expected = 'ab', 'eidboaoo', False
    print(obj.checkInclusion(s1, s2) == expected)

    s1, s2, expected = 'ab', 'ba', True
    print(obj.checkInclusion(s1, s2) == expected)

    s1, s2, expected = 'abb', 'ba', False
    print(obj.checkInclusion(s1, s2) == expected)

    s1, s2, expected = 'ba', 'cab', True
    print(obj.checkInclusion(s1, s2) == expected)

# last line of code
