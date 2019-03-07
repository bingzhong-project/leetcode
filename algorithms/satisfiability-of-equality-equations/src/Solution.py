class Solution:
    def equationsPossible(self, equations: 'List[str]') -> 'bool':
        def cursor(str):
            return ord(str) % ord('A')

        adj = [[] for _ in range(cursor('z') + 1)]
        unconnected = []
        for equation in equations:
            a = cursor(equation[0])
            symbol = equation[1]
            b = cursor(equation[3])
            if symbol == '=':
                adj[a].append(b)
                adj[b].append(a)
            else:
                unconnected.append((a, b))

        for a, b in unconnected:
            queue = []
            queue.append(a)
            visited = set()
            while queue:
                e = queue.pop(0)
                if e == b:
                    return False
                visited.add(e)
                for c in adj[e]:
                    if c not in visited:
                        queue.append(c)

        return True
