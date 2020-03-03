# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        def tree2array(root):
            if root is None:
                return []
            left_array = tree2array(root.left)
            right_array = tree2array(root.right)

            return left_array + [root.val] + right_array

        def array2tree(array):
            if len(array) == 0:
                return None
            max_val = max(array)
            index = array.index(max_val)
            node = TreeNode(max_val)
            node.left = array2tree(array[:index])
            node.right = array2tree(array[index + 1:])
            return node

        array = tree2array(root)
        array.append(val)

        return array2tree(array)
