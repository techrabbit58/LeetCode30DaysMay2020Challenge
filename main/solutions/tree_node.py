"""
A node type for making up binary trees, like BSTs.
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.__class__.__name__}(val={self.val}, left={self.left}, right={self.right})'

    def breadth_traversal(self):
        q = deque([self])
        answer = []
        while q:
            node = q.popleft()
            if node:
                answer.append(node.val)
                if node.left or node.right:
                    q.append(node.left)
                    q.append(node.right)
            else:
                answer.append(None)
        return answer

# last line of code
