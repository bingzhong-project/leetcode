import collections


class Solution:
    def calcEquation(self, equations: 'List[List[str]]', values: 'List[float]',
                     queries: 'List[List[str]]') -> 'List[float]':
        NONENTITY = float(-1)

        adj = collections.defaultdict(list)
        elements = set()
        for i in range(len(equations)):
            equation = equations[i]
            value = values[i]
            dividend = equation[0]
            divisor = equation[1]
            adj[dividend] += [(divisor, value)]
            adj[divisor] += [(dividend, 1 / value)]
            elements.add(dividend)
            elements.add(divisor)
        res = [NONENTITY for _ in range(len(queries))]
        for i in range(len(queries)):
            query = queries[i]
            if query[0] not in elements or query[1] not in elements:
                continue
            if query[0] == query[1]:
                res[i] = float(1)
                continue
            queue = []
            visited = set()
            res_ans = 1
            queue.append((query[0], 1))
            found = False
            while queue and not found:
                node, ans = queue.pop(0)
                for next_node, value in adj[node]:
                    if next_node in visited:
                        continue
                    visited.add(next_node)
                    if next_node == query[1]:
                        found = True
                        res_ans = ans * value
                        break
                    else:
                        queue.append((next_node, ans * value))
            if found:
                res[i] = res_ans

        return res
