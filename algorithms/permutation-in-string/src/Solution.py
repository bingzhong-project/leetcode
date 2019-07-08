import collections


class Solution:
    def checkInclusion(self, s1: 'str', s2: 'str') -> 'bool':
        counter = collections.Counter()
        keys = set()
        for s in s1:
            counter[s] += 1
            keys.add(s)
        left = 0
        right = 0
        length = len(counter)
        while right < len(s2):
            s = s2[right]
            if s in counter and counter[s] > 0:
                counter[s] -= 1
            else:
                if s2[left] in keys:
                    counter[s2[left]] += 1
                    length += 1
                left += 1
            if counter[s] == 0:
                length -= 1
            if length == 0:
                return True
            right += 1

        return length == 0


if __name__ == "__main__":
    print(Solution().checkInclusion(s1="adc", s2="dcda"))
    # print(Solution().checkInclusion(s1="ab", s2="eidbaooo"))
    # print(Solution().checkInclusion(s1="ab", s2="eidboaoo"))
    # print(Solution().checkInclusion(s1="ccc", s2="cbac"))
    # print(Solution().checkInclusion(s1="a", s2="a"))
    # print(Solution().checkInclusion("pqzhi", "ghrqpihzybre"))
    # print(Solution().checkInclusion(
    # "trinitrophenylmethylnitramine",
    # "dinitrophenylhydrazinetrinitrophenylmethylnitramine"))
    print(Solution().checkInclusion("hello", "ooolleoooleh"))
