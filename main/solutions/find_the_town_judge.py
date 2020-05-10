"""
Week 2, Day 2: Find the Town Judge

In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town
judge.

If the town judge exists, then:

    - The town judge trusts nobody.
    - Everybody (except for the town judge) trusts the town judge.
    - There is exactly one person that satisfies properties 1 and 2.

You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person
labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

E x a m p l e s

    Input: N = 2, trust = [[1,2]]
    Output: 2

    Input: N = 3, trust = [[1,3],[2,3]]
    Output: 3

    Input: N = 3, trust = [[1,3],[2,3],[3,1]]
    Output: -1

    Input: N = 3, trust = [[1,2],[2,3]]
    Output: -1

    Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    Output: 3

N o t e s

    - 1 <= N <= 1000
    - trust.length <= 10000
    - trust[i] are all different
    - trust[i][0] != trust[i][1]
    - 1 <= trust[i][0], trust[i][1] <= N

"""
from collections import defaultdict
from time import perf_counter_ns
from typing import List


def findJudge(N: int, trust: List[List[int]]) -> int:
    """Complexity: O(n)"""
    if not trust:
        return -1 if N > 1 else 1
    confidence = defaultdict(int)
    believers = set()
    for a, b in trust:
        confidence[b] += 1
        believers.add(a)
    judge = {confidant
             for confidant, num_believers in confidence.items()
             if num_believers == N - 1 and confidant not in believers}
    return -1 if not judge else judge.pop()


def findJudge_v2(N: int, trust: List[List[int]]) -> int:
    """
    This version is inspired by a post found in a LeetCode discussion.
    https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3325/discuss/244859/Python-O(n)-with-Explanation
    It is less complicated, and it is slightly faster.
    Complexity: O(n)
    """
    confidence = {b: 0 for b in range(1, N + 1)}
    for a, b in trust:
        confidence[a] -= 1
        confidence[b] += 1
    judge = {a for a, b in confidence.items() if b == N - 1}
    return -1 if not judge else judge.pop()


if __name__ == '__main__':

    start = perf_counter_ns()
    print(findJudge(N=1, trust=[]) == 1)
    print(findJudge(N=2, trust=[[1, 2]]) == 2)
    print(findJudge(N=3, trust=[[1, 3], [2, 3]]) == 3)
    print(findJudge(N=3, trust=[[1, 3], [2, 3], [3, 1]]) == -1)
    print(findJudge(N=3, trust=[[1, 2], [2, 3]]) == -1)
    print(findJudge(N=4, trust=[[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]) == 3)
    print('v1', perf_counter_ns() - start)

    start = perf_counter_ns()
    print(findJudge_v2(N=1, trust=[]) == 1)
    print(findJudge_v2(N=2, trust=[[1, 2]]) == 2)
    print(findJudge_v2(N=3, trust=[[1, 3], [2, 3]]) == 3)
    print(findJudge_v2(N=3, trust=[[1, 3], [2, 3], [3, 1]]) == -1)
    print(findJudge_v2(N=3, trust=[[1, 2], [2, 3]]) == -1)
    print(findJudge_v2(N=4, trust=[[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]) == 3)
    print('v2', perf_counter_ns() - start)

# last line of code
