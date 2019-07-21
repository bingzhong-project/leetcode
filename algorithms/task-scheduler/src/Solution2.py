import collections


class Solution:
    def leastInterval(self, tasks: 'List[str]', n: 'int') -> 'int':
        counter = collections.Counter(tasks)
        max_frequency_task = max(counter, key=counter.get)
        max_frequency = counter[max_frequency_task]
        idle = n * (max_frequency - 1)
        for task, count in counter.items():
            if task == max_frequency_task:
                continue
            idle -= min(count, max_frequency - 1)
        return len(tasks) + max(idle, 0)
