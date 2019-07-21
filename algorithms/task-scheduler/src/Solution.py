class Solution:
    def leastInterval(self, tasks: 'List[str]', n: 'int') -> 'int':
        counter = [0 for _ in range(26)]
        for task in tasks:
            counter[ord(task) - ord('A')] += 1
        counter.sort()
        max_frequency = counter[-1]
        i = 25
        while i > 0 and counter[i] == max_frequency:
            i -= 1
        return max((max_frequency - 1) * (n + 1) + (25 - i), len(tasks))
