"""
Week 1, Day 7: Cousins in Binary Tree

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different
nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

Example 1:

    Input: root = [1,2,3,4], x = 4, y = 3
    Output: false

Example 2:

    Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
    Output: true

Example 3:

    root = [1,2,3,null,4], x = 2, y = 3
    Output: false

Notes:

    1. The number of nodes in the tree will be between 2 and 100.
    2. Each node has a unique integer value from 1 to 100.

"""
from collections import deque

from solutions.tree_node import TreeNode


def isCousins(root: TreeNode, x: int, y: int) -> bool:
    queue = deque()
    queue.append((0, root))
    candidates = {}
    while queue:
        depth, node = queue.popleft()
        if len(candidates) >= 2:
            break
        if node.left:
            queue.append((depth + 1, node.left))
            if node.left.val in {x, y}:
                candidates[node.left.val] = (depth + 1, node.val)
        if node.right:
            queue.append((depth + 1, node.right))
            if node.right.val in {x, y}:
                candidates[node.right.val] = (depth + 1, node.val)
    return len(candidates) > 1 and candidates[x][0] == candidates[y][0] and candidates[x][1] != candidates[y][1]


if __name__ == '__main__':
    
    root = TreeNode(1, left=TreeNode(2, left=TreeNode(4)), right=TreeNode(3))
    x = 4
    y = 3
    print(isCousins(root, x, y) is False)
    
    root = TreeNode(1, left=TreeNode(2, right=TreeNode(4)), right=TreeNode(3, right=TreeNode(5)))
    x = 5
    y = 4
    print(isCousins(root, x, y) is True)

    root = TreeNode(1, left=TreeNode(2, right=TreeNode(4)), right=TreeNode(3))
    x = 2
    y = 3
    print(isCousins(root, x, y) is False)

    root = TreeNode(1, right=TreeNode(2, left=TreeNode(3, right=TreeNode(4, right=TreeNode(5)))))
    x = 1
    y = 3
    print(isCousins(root, x, y) is False)

    root = TreeNode(1, left=TreeNode(2, right=TreeNode(3, right=TreeNode(4, left=TreeNode(5)))))
    x = 3
    y = 4
    print(isCousins(root, x, y) is False)

# last line of code
