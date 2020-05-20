"""
Week 3, Day 6: Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

H i n t s

(1) Try to utilize the property of a BST.
(2) Try in-order traversal.
(3) What if you could modify the BST node's structure?
(4) The optimal runtime complexity is O(height of BST).

E x a m p l e s

    Input: root = [3,1,4,null,2], k = 1
      3
     / \
    1   4
     \
      2
    Output: 1
    ---------------
    Input: root = [5,3,6,2,4,null,null,1], k = 3
          5
         / \
        3   6
       / \
      2   4
     /
    1
    Output: 3
    ---------------
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack, node, val = [], root, None
        while k:
            if node:
                stack.append(node)
                node = node.left
                continue
            node = stack.pop()
            k -= 1
            val = node.val
            node = node.right
        return val


class SolutionV2:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack, node = [], root
        while True:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if not k:
                return node.val
            node = node.right


if __name__ == '__main__':
    
    o = Solution()

    root = TreeNode(42)
    k = 1
    expected = 42
    print(o.kthSmallest(root, k) == expected)

    root = TreeNode(3, left=TreeNode(1, right=TreeNode(2)), right=TreeNode(4))
    k = 1
    expected = 1
    print(o.kthSmallest(root, k) == expected)

    root = TreeNode(5, left=TreeNode(3, left=TreeNode(2, left=TreeNode(1)), right=TreeNode(4)), right=TreeNode(6))
    k = 3
    expected = 3
    print(o.kthSmallest(root, k) == expected)

# last line of code
