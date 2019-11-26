# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def nextLargerNodes(self, head: ListNode) -> list:
        cache = {}
        stack = []
        node = head
        index = 0
        while node:
            while stack and stack[-1][1] < node.val:
                cache[stack.pop()[0]] = node.val
            stack.append((index, node.val))
            node = node.next
            index += 1

        array = [0 for _ in range(index)]
        for i in range(len(array)):
            if i in cache:
                array[i] = cache[i]

        return array
