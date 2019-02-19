# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        res = []
        stack = []
        node = root
        last = None

        while node or stack:
            pass

        return res
