# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        copies = {}
        visited = set()
        queue = [node]
        visited.add(node)
        while queue:
            n = queue.pop(0)
            if n.val not in copies:
                copies[n.val] = Node(n.val, [])
            for nei in n.neighbors:
                if nei.val not in copies:
                    copies[nei.val] = Node(nei.val, [])
                copies[n.val].neighbors.append(copies[nei.val])
                if nei not in visited:
                    queue.append(nei)
                    visited.add(nei)

        return copies[node.val]
