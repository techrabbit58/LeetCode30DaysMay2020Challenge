"""
Week 5, Day 1: Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first
take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for
you to finish all courses?

Example 1:

    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take.
                 To take course 1 you should have finished course 0. So it is possible.

Example 2:

    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take.
                 To take course 1 you should have finished course 0, and to take course 0 
                 you should also have finished course 1. So it is impossible.

Constraints:

    The input prerequisites is a graph represented by a list of edges, not adjacency
    matrices. Read more about how a graph is represented.

    You may assume that there are no duplicate edges in the input prerequisites.

    1 <= numCourses <= 10^5

Hints:

    This problem is equivalent to finding if a cycle exists in a directed graph.
    If a cycle exists, no topological ordering exists and therefore it will be
    impossible to take all courses.

"""
from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        follower_of = defaultdict(list)
        for a, b in prerequisites:
            follower_of[a].append(b)

        def is_cyclic(course: int, visited: List[bool], stack: List[bool]) -> bool:
            visited[course] = True
            stack[course] = True
            for neighbour in follower_of[course]:
                if not visited[neighbour]:
                    if is_cyclic(neighbour, visited, stack):
                        return True
                elif stack[neighbour]:
                    return True
            stack[course] = False
            return False

        visited = [False] * numCourses
        stack = [False] * numCourses
        for course in range(numCourses):
            if not visited[course]:
                if is_cyclic(course, visited, stack):
                    return False
        return True


if __name__ == '__main__':
    o = Solution()

    print(o.canFinish(2, [[1, 0]]), True)
    print(o.canFinish(2, [[1, 0], [0, 1]]), False)
    print(o.canFinish(4, [[0, 1], [1, 2], [2, 3], [0, 2], [2, 0], [3, 3]]), False)
    print(o.canFinish(4, [[0, 1], [1, 2], [2, 3], [0, 2]]), True)

# last line of code
