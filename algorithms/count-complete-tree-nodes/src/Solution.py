# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: 'TreeNode') -> 'int':
        def count(node):
            left_hight = 0
            right_hight = 0
            left_node = node
            right_node = node
            while left_node:
                left_hight += 1
                left_node = left_node.left
            while right_node:
                right_hight += 1
                right_node = right_node.right
            if left_hight == right_hight:
                return 2**left_hight - 1
            else:
                return count(node.left) + count(node.right) + 1

        return count(root)
