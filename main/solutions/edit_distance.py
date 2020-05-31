"""
Week 5, Day 3: Edit Distance

Given two words word1 and word2, find the minimum number of operations required to convert
word1 to word2.

You have the following 3 operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character

Example 1:

    Input: word1 = "horse", word2 = "ros"
    Output: 3
    Explanation:
        horse -> rorse (replace 'h' with 'r')
        rorse -> rose (remove 'r')
        rose -> ros (remove 'e')

Example 2:

    Input: word1 = "intention", word2 = "execution"
    Output: 5
    Explanation:
        intention -> inention (remove 't')
        inention -> enention (replace 'i' with 'e')
        enention -> exention (replace 'n' with 'x')
        exention -> exection (replace 'n' with 'c')
        exection -> execution (insert 'u')
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Levenshtein algorithm, plus dynamic programming.
        Ref.: https://en.wikipedia.org/wiki/Edit_distance
        Ref.: https://en.wikipedia.org/wiki/Levenshtein_distance
        A standard of word processing.
        :param word1: a string
        :param word2: another string
        :return: Levenshtein distance of both words
        """
        M, N = len(word1), len(word2)
        mem = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(1, M + 1):  # cost for deletion of word 1
            mem[i][0] = i
        for j in range(1, N + 1):  # cost for deletion of word 2
            mem[0][j] = j
        for j, a in enumerate(word2, 1):
            for i, b in enumerate(word1, 1):
                k = 0 if a == b else 1
                i1, j1 = i - 1, j - 1
                mem[i][j] = min(
                    mem[i1][j] + 1,  # deletion
                    mem[i][j1] + 1,  # insertion
                    mem[i1][j1] + k  # substitution
                )
        return mem[-1][-1]


if __name__ == '__main__':
    o = Solution()

    print(o.minDistance(word1='kitten', word2='sitting') == 3)
    print(o.minDistance(word1="horse", word2="ros") == 3)
    print(o.minDistance(word1="intention", word2="execution") == 5)
    print(o.minDistance(word1='', word2='a') == 1)
    print(o.minDistance(word1='a', word2='b') == 1)
    print(o.minDistance(word1='a', word2='a') == 0)
    print(o.minDistance(word1='a', word2='ab') == 1)
    print(o.minDistance(word1='ba', word2='ab') == 2)

# last line of code
