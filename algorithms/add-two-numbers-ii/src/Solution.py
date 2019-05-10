# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        if l1.val == 0 and l2.val == 0:
            return ListNode(0)
        lenght1 = 0
        node = l1
        while node:
            lenght1 += 1
            node = node.next

        lenght2 = 0
        node = l2
        while node:
            lenght2 += 1
            node = node.next
        if lenght2 > lenght1:
            temp = l1
            l1 = l2
            l2 = temp
            temp = lenght1
            lenght1 = lenght2
            lenght2 = temp
        length = max(lenght1, lenght2)
        node1 = l1
        node2 = l2
        ans = []
        while length > 0:
            val1 = node1.val
            val2 = 0 if length > lenght2 else node2.val
            val = val1 + val2
            if val > 9:
                val %= 10
                if ans:
                    ans[-1] += 1
                else:
                    ans.append(1)
            ans.append(val)
            node1 = node1.next
            node2 = node2 if length > lenght2 else node2.next
            length -= 1

        sentinel = ListNode(None)
        pre = sentinel
        for i in range(len(ans) - 1, -1, -1):
            if ans[i] > 9:
                ans[i] %= 10
                if i - 1 >= 0:
                    ans[i - 1] += 1
        if ans[0] == 0:
            ans.insert(0, 1)
        for num in ans:
            node = ListNode(num)
            pre.next = node
            pre = node
        return sentinel.next
