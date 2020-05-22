"""
Week 4, Day 1: Sort Characters By Frequency

Given a string, sort it in decreasing order based on the frequency of characters.
"""
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        frequencies = Counter(s)
        return ''.join([c[0] * c[1] for c in frequencies.most_common()])


if __name__ == '__main__':
    o = Solution()

    print(o.frequencySort('tree'), 'eetr')
    print(o.frequencySort('cccaaa'), 'cccaaa')
    print(o.frequencySort('Aabb'), 'bbAa')

# last line of code
