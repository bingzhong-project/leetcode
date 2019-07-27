class Solution:
    def findLongestChain(self, pairs: 'List[List[int]]') -> 'int':
        pairs.sort(key=lambda x: x[0])
        res = 1
        cur = pairs[0][1]
        for i in range(1, len(pairs)):
            pair = pairs[i]
            if cur >= pair[0]:
                cur = min(cur, pair[1])
            else:
                cur = pair[1]
                res += 1
        return res
