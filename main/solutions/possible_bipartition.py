"""
Week 4, Day 6: Possible Bipartition

Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into
two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered
a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.

Example 1:

    Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
    Output: true
    Explanation: group1 [1,4], group2 [2,3]

Example 2:

    Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
    Output: false

Example 3:

    Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
    Output: false
 
Note:

    1 <= N <= 2000
    0 <= dislikes.length <= 10000
    1 <= dislikes[i][j] <= N
    dislikes[i][0] < dislikes[i][1]

    There does not exist i != j for which dislikes[i] == dislikes[j].

"""
from typing import List


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        """
        Slow, but it works. The problem to solve is equivalent to the bipartite graph
        problem. We can interpret the two groups as to colors. A graph can be seen as
        a bipartitionable graph, described by two disjunct sets of vertices U and V, and a
        set of edges E. The union of U and V is bipartite, if any two neighboring vertices
        can be colored with two different colors. The algorithm tries to color each neighbored
        vertices in to different colors, with only two colors at all, and gives True for bipartite
        if coloring is possible, and Fase in any other case. Time complexity is O(n^2). Space
        complexity is also O(n^2), because the graph is represented as a 2D matrix with n*n
        cells (with n being the number of vertices |U|+|V|).

        Please see Wikipedia for reference:
        https://en.wikipedia.org/wiki/Bipartite_graph

        Another solution with time complexity O(n) and aux. space complexity O(n) is given here:
        https://www.geeksforgeeks.org/check-if-a-given-graph-is-bipartite-using-dfs/?ref=rp
        I guess it will be executed significantly faster. But have not tried yet.
        """
        ALT_COLOR = [1, 0]
        UNDYED = -1
        if not dislikes:
            return True
        graph = [[0] * N for _ in range(N)]
        for a, b in dislikes:
            graph[a - 1][b - 1] = graph[b - 1][a - 1] = 1
        colors = [1] + [UNDYED] * (N - 1)
        stack = list(reversed([n for n in range(N)]))
        while stack:
            u = stack.pop()
            for v in range(N):
                if graph[u][v]:
                    if colors[v] == UNDYED:
                        colors[v] = ALT_COLOR[colors[u]]
                        stack.append(v)
                    elif colors[v] == colors[u]:
                        return False
        return True


if __name__ == '__main__':
    o = Solution()

    N = 4
    dislikes = [[1, 2], [1, 3], [2, 4]]
    expected = True
    print(o.possibleBipartition(N, dislikes) == expected)

    N = 3
    dislikes = [[1, 2], [1, 3], [2, 3]]
    expected = False
    print(o.possibleBipartition(N, dislikes) == expected)

    N = 5
    dislikes = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
    expected = False
    print(o.possibleBipartition(N, dislikes) == expected)

    N = 10
    dislikes = [[4, 7], [4, 8], [2, 8], [8, 9], [1, 6], [5, 8], [1, 2], [6, 7], [3, 10], [8, 10], [1, 5], [
        7, 10], [1, 10], [3, 5], [3, 6], [1, 4], [3, 9], [2, 3], [1, 9], [7, 9], [2, 7], [6, 8], [5, 7], [3, 4]]
    expected = True
    print(o.possibleBipartition(N, dislikes) == expected)

    N = 50
    dislikes = [
        [21, 47], [4, 41], [2, 41], [36, 42], [32, 45], [26, 28], [32, 44], [5, 41],
        [29, 44], [10, 46], [1, 6], [7, 42], [46, 49], [17, 46], [32, 35], [11, 48],
        [37, 48], [37, 43], [8, 41], [16, 22], [41, 43], [11, 27], [22, 44], [22, 28],
        [18, 37], [5, 11], [18, 46], [22, 48], [1, 17], [2, 32], [21, 37], [7, 22],
        [23, 41], [30, 39], [6, 41], [10, 22], [36, 41], [22, 25], [1, 12], [2, 11],
        [45, 46], [2, 22], [1, 38], [47, 50], [11, 15], [2, 37], [1, 43], [30, 45],
        [4, 32], [28, 37], [1, 21], [23, 37], [5, 37], [29, 40], [6, 42], [3, 11],
        [40, 42], [26, 49], [41, 50], [13, 41], [20, 47], [15, 26], [47, 49], [5, 30],
        [4, 42], [10, 30], [6, 29], [20, 42], [4, 37], [28, 42], [1, 16], [8, 32],
        [16, 29], [31, 47], [15, 47], [1, 5], [7, 37], [14, 47], [30, 48], [1, 10],
        [26, 43], [15, 46], [42, 45], [18, 42], [25, 42], [38, 41], [32, 39], [6, 30],
        [29, 33], [34, 37], [26, 38], [3, 22], [18, 47], [42, 48], [22, 49], [26, 34],
        [22, 36], [29, 36], [11, 25], [41, 44], [6, 46], [13, 22], [11, 16], [10, 37],
        [42, 43], [12, 32], [1, 48], [26, 40], [22, 50], [17, 26], [4, 22], [11, 14],
        [26, 39], [7, 11], [23, 26], [1, 20], [32, 33], [30, 33], [1, 25], [2, 30],
        [2, 46], [26, 45], [47, 48], [5, 29], [3, 37], [22, 34], [20, 22], [9, 47],
        [1, 4], [36, 46], [30, 49], [1, 9], [3, 26], [25, 41], [14, 29], [1, 35],
        [23, 42], [21, 32], [24, 46], [3, 32], [9, 42], [33, 37], [7, 30], [29, 45],
        [27, 30], [1, 7], [33, 42], [17, 47], [12, 47], [19, 41], [3, 42], [24, 26],
        [20, 29], [11, 23], [22, 40], [9, 37], [31, 32], [23, 46], [11, 38], [27, 29],
        [17, 37], [23, 30], [14, 42], [28, 30], [29, 31], [1, 8], [1, 36], [42, 50],
        [21, 41], [11, 18], [39, 41], [32, 34], [6, 37], [30, 38], [21, 46], [16, 37],
        [22, 24], [17, 32], [23, 29], [3, 30], [8, 30], [41, 48], [1, 39], [8, 47],
        [30, 44], [9, 46], [22, 45], [7, 26], [35, 42], [1, 27], [17, 30], [20, 46],
        [18, 29], [3, 29], [4, 30], [3, 46]
    ]
    expected = True
    print(o.possibleBipartition(N, dislikes) == expected)

    N = 5
    dislikes = [[1, 2], [3, 4], [4, 5], [3, 5]]
    expected = False
    print(o.possibleBipartition(N, dislikes) == expected)

# last line of code
