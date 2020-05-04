"""
Week 1, Day 2: Jewels And Stones

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive,
so "a" is considered a different type of stone from "A".

N O T E :
- S and J will consist of letters and have length at most 50.
- The characters in J are distinct.
- Hint: For each stone, check if it is a jewel.

E X A M P L E S

    Input: J = "aA", S = "aAAbbbb"
    Output: 3

    Input: J = "z", S = "ZZ"
    Output: 0

"""
from collections import Counter, defaultdict


def numJewelsInStones(J: str, S: str) -> int:
    return sum(value for key, value in Counter(S).items() if key in J)


def numJewelsInStones_v2(J: str, S: str) -> int:
    jewels, stones, counts = set(J), list(S), 0
    for s in stones:
        if s in jewels:
            counts += 1
    return counts


def numJewelsInStones_v3(J: str, S: str) -> int:
    return len([s for s in list(S) if s in set(J)])


def numJewelsInStones_v4(J: str, S: str) -> int:
    """This seams to be the fastest solution. At least from point of view of the LeetCode solution runner."""
    counts = defaultdict(int)
    for j in J:
        counts[j] += S.count(j)
    return sum(counts.values())


if __name__ == '__main__':
    assert numJewelsInStones_v4('aA', 'aAAbbbb') == 3
    assert numJewelsInStones_v4('z', 'ZZ') == 0

# last line of code
