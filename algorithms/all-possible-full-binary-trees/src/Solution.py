# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def allPossibleFBT(self, N: int) -> list:
        def func(n):
            if n % 2 == 0:
                return []
            if n == 1:
                return [TreeNode(0)]
            res = []

            for i in range(n - 1):
                left_trees = func(i)
                right_trees = func(n - 1 - i)
                for left_tree in left_trees:
                    for right_tree in right_trees:
                        node = TreeNode(0)
                        node.left = left_tree
                        node.right = right_tree
                        res.append(node)
            
            return res

        return func(N)
