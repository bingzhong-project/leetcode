# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findFrequentTreeSum(self, root: 'TreeNode') -> 'List[int]':
        if root is None:
            return []
        self.frequent = {}
        self.max = 0
        self.res = []

        self.treeSum(root)
        return self.res

    def treeSum(self, root):
        if root is None:
            return 0
        left_sum = self.treeSum(root.left)
        right_sum = self.treeSum(root.right)
        sum = root.val + left_sum + right_sum
        if sum in self.frequent:
            self.frequent[sum] += 1
        else:
            self.frequent[sum] = 1
        if self.frequent[sum] > self.max:
            self.max = self.frequent[sum]
            self.res = [sum]
        elif self.frequent[sum] == self.max:
            self.res.append(sum)
        return sum
