class TreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if self.root:
            return self.book0(self.root, start, end)
        self.root = TreeNode(start, end)
        return True

    def book0(self, node, start, end):
        if start >= node.end:
            if node.right:
                return self.book0(node.right, start, end)
            node.right = TreeNode(start, end)
            return True
        if end <= node.start:
            if node.left:
                return self.book0(node.left, start, end)
            node.left = TreeNode(start, end)
            return True

        return False
