"""
Week 1, Day 3: Ransom Note

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function
that will return true if the ransom note can be constructed from the magazines; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note: You may assume that both strings contain only lowercase letters.

E x a m p l e s

    canConstruct("a", "b") -> false
    canConstruct("aa", "ab") -> false
    canConstruct("aa", "aab") -> true

"""
from collections import Counter


def canConstruct(ransomNote: str, magazine: str) -> bool:
    r = Counter(ransomNote)
    m = Counter(magazine)
    for letter, count in r.items():
        if count > m[letter]:
            return False
    return True


def canConstruct_v2(ransomNote: str, magazine: str) -> bool:
    """The LeetCode solution runner judges this as the fastest solution of all four."""
    for letter in set(ransomNote):
        if ransomNote.count(letter) > magazine.count(letter):
            return False
    return True


def canConstruct_v3(ransomNote: str, magazine: str) -> bool:
    return all(ransomNote.count(letter) <= magazine.count(letter) for letter in set(ransomNote))


def canConstruct_v4(ransomNote: str, magazine: str) -> bool:
    """I like this solution most."""
    return not any(ransomNote.count(letter) > magazine.count(letter) for letter in set(ransomNote))


def canConstruct_v5(ransomNote: str, magazine: str) -> bool:
    requirement = Counter(ransomNote)
    return requirement == requirement & Counter(magazine)


def canConstruct_v6(ransomNote: str, magazine: str) -> bool:
    """
    This solution, I picked from the problem discussion page.
    Contributed by user 'siwal'.
    I liked the intuitive and straight forward approach:
        1) Take the next letter from the note.
        2) If the required record is not found in a magazine, we can not compose the given note.
            2a) Stop pointless.
        3) Otherwise, cut out the letter and advance. The magazines now have one more cutout and one less letter.
        4) Repeat 1 to 3 until note is complete.
        5) Success!
    Nice! Easy to understand!
    """
    for letter in ransomNote:
        if letter not in magazine:
            return False
        else:
            magazine = magazine.replace(letter, '', 1)
    return True


if __name__ == '__main__':
    print(canConstruct_v6('a', 'b'), False)
    print(canConstruct_v6('aa', 'ab'), False)
    print(canConstruct_v6('aa', 'aab'), True)

# last line of code
