"""
Week 4, Day 3: Construct Binary Search Tree from Preorder Traversal

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has
a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder
traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree
with the given requirements.

Constraints:

    1 <= preorder.length <= 100
    1 <= preorder[i] <= 10^8
    The values of preorder are distinct.

"""
from itertools import islice
from typing import List

from solutions.tree_node import TreeNode


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        node_stack = []
        node = root = TreeNode(preorder[0])
        for n in islice(preorder, 1, None):
            if n <= node.val:
                node.left = TreeNode(n)
                node_stack.append(node)
                node = node.left
            else:
                while node_stack and n > node_stack[-1].val:
                    node = node_stack.pop()
                node.right = TreeNode(n)
                node = node.right
        return root


if __name__ == '__main__':

    # root = TreeNode(8, left=TreeNode(5, left=TreeNode(1), right=TreeNode(7)), right=TreeNode(10, right=TreeNode(12)))
    # print(root.breadth_traversal() == [8, 5, 10, 1, 7, None, 12])

    o = Solution()

    example = [8, 5, 1, 7, 10, 12]
    expected = [8, 5, 10, 1, 7, None, 12]
    print(o.bstFromPreorder(example).breadth_traversal() == expected)

# last line of code
