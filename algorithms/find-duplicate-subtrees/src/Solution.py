# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findDuplicateSubtrees(self, root: 'TreeNode') -> 'List[TreeNode]':
        def dfs(root, sub_trees, duplicates, res):
            if root is None:
                return "N"
            left_tree = dfs(root.left, sub_trees, duplicates, res)
            if left_tree in sub_trees and left_tree not in duplicates:
                res.append(root.left)
                duplicates.add(left_tree)
            sub_trees.add(left_tree)

            right_tree = dfs(root.right, sub_trees, duplicates, res)
            if right_tree in sub_trees and right_tree not in duplicates:
                res.append(root.right)
                duplicates.add(right_tree)
            sub_trees.add(right_tree)

            return str(root.val) + left_tree + right_tree

        res = []
        dfs(root, set(), {"N"}, res)
        return res
