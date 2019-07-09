import collections


class Solution:
    def checkInclusion(self, s1: 'str', s2: 'str') -> 'bool':
        counter = collections.Counter()
        for s in s1:
            counter[s] += 1
        length = len(counter)

        left = 0
        right = 0
        while right < len(s2):
            s = s2[right]
            if s in counter:
                counter[s] -= 1
                if counter[s] == 0:
                    length -= 1
            right += 1
            while length == 0:
                if s2[left] in counter:
                    counter[s2[left]] += 1
                    if counter[s2[left]] > 0:
                        length += 1
                if right - left == len(s1):
                    return True
                left += 1
        return False
