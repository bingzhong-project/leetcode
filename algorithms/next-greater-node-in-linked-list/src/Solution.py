# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def nextLargerNodes(self, head: ListNode) -> list:
        stack = []
        node = head
        while node:
            while stack and stack[-1] < node.val:
                stack.pop()
