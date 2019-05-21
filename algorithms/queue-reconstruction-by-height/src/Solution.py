import collections


class Solution:
    def reconstructQueue(self, people: 'List[List[int]]') -> 'List[List[int]]':
        position = [i for i in range(len(people))]
        people_map = collections.defaultdict(list)
        for i in range(len(people)):
            people_map[people[i][0]] += [people[i][1]]
        height = sorted(list(people_map.keys()))
        queue = [None for i in range(len(people))]
        for h in height:
            for l in sorted(list(people_map[h]), reverse=True):
                queue[position[l]] = [h, l]
                del position[l]

        return queue
