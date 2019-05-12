# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: 'TreeNode', s: 'int') -> 'int':
        def func(node, res):
            if node.val == s:
                res[0] += 1
            node_sums = [node.val]
            left_sums = []
            right_sums = []
            if node.left:
                left_sums = func(node.left, res)
            if node.right:
                right_sums = func(node.right, res)
            for left_sum in left_sums:
                temp = left_sum + node.val
                if temp == s:
                    res[0] += 1
                node_sums.append(temp)
            for right_sum in right_sums:
                temp = right_sum + node.val
                if temp == s:
                    res[0] += 1
                node_sums.append(temp)
            return node_sums

        res = [0]
        if root:
            func(root, res)
        return res[0]
