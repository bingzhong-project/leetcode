import collections


class Solution:
    def reconstructQueue(self, people: 'List[List[int]]') -> 'List[List[int]]':
        people_map = collections.defaultdict(list)
        for p in people:
            people_map[p[0]] += [p[1]]
        height = sorted(list(people_map.keys()), reverse=True)
        queue = []
        for h in height:
            for pos in sorted(people_map[h]):
                queue.insert(pos, [h, pos])
        return queue
