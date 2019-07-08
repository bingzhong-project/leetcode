import collections


class Solution:
    def checkInclusion(self, s1: 'str', s2: 'str') -> 'bool':
        """TLE
        """
        counter = collections.Counter()
        for s in s1:
            counter[s] += 1
        backup = counter.copy()
        left = 0
        right = len(s1)
        while right <= len(s2):
            for i in range(left, right):
                s = s2[i]
                if s in counter:
                    counter[s] -= 1
                    if counter[s] == 0:
                        del counter[s]
                    if len(counter) == 0:
                        return True
                else:
                    break
            counter = backup.copy()
            left += 1
            right += 1

        return len(counter) == 0


if __name__ == "__main__":
    print(Solution().checkInclusion(s1="adc", s2="dcda"))
    print(Solution().checkInclusion(s1="ab", s2="eidbaooo"))
    print(Solution().checkInclusion(s1="ab", s2="eidboaoo"))
    print(Solution().checkInclusion(s1="ccc", s2="cbac"))
    print(Solution().checkInclusion(s1="a", s2="a"))
