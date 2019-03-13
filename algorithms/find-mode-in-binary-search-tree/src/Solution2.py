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
        self.prev_num = None
        self.num_count = 1
        self.max_count = 0
        self.res = []
        self.inorder(root)
        if self.num_count > self.max_count:
            self.res = []
            self.res.append(self.prev_num)
            self.max_count = self.num_count
        elif self.num_count == self.max_count:
            self.res.append(self.prev_num)
        return self.res

    def inorder(self, node):
        if node.left:
            self.inorder(node.left)
        if self.prev_num == node.val:
            self.num_count += 1
        elif self.prev_num is not None:
            if self.num_count > self.max_count:
                self.res = []
                self.res.append(self.prev_num)
                self.max_count = self.num_count
            elif self.num_count == self.max_count:
                self.res.append(self.prev_num)
            self.num_count = 1
        self.prev_num = node.val
        if node.right:
            self.inorder(node.right)
