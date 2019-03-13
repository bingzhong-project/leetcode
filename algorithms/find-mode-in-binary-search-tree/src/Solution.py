# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: 'TreeNode') -> 'List[int]':
        if root is None:
            return []
        res = []
        max_count = 0
        prev_num = None
        num_count = 1
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            if stack:
                node = stack.pop()
                if prev_num == node.val:
                    num_count += 1
                elif prev_num is not None:
                    if num_count > max_count:
                        res = []
                        res.append(prev_num)
                        max_count = num_count
                    elif num_count == max_count:
                        res.append(prev_num)
                    num_count = 1
                prev_num = node.val
            node = node.right
        if num_count > max_count:
            res = []
            res.append(prev_num)
            max_count = num_count
        elif num_count == max_count:
            res.append(prev_num)
        return res
