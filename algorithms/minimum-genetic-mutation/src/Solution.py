class Solution:
    def minMutation(self, start: 'str', end: 'str',
                    bank: 'List[str]') -> 'int':
        def conversion(source, target):
            if len(source) != len(target):
                return False
            diff = 0
            for i in range(len(source)):
                if source[i] != target[i]:
                    diff += 1
                if diff > 1:
                    break
            return diff == 1

        bank = set(bank)
        if end not in bank:
            return -1
        ans = 0
        queue = []
        queue.append(start)
        while queue:
            ans += 1
            for _ in range(len(queue)):
                node = queue.pop(0)
                remove = set()
                for next_node in bank:
                    if conversion(node, next_node):
                        if next_node == end:
                            return ans
                        remove.add(next_node)
                        queue.append(next_node)
                bank -= remove
        return -1
