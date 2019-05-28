import collections


class Solution:
    def fourSumCount(self, A: 'List[int]', B: 'List[int]', C: 'List[int]',
                     D: 'List[int]') -> 'int':
        AB = collections.Counter()
        N = len(A)
        for i in range(N):
            for j in range(N):
                AB[A[i] + B[j]] += 1
        res = 0
        for i in range(N):
            for j in range(N):
                target = -(C[i] + D[j])
                res += AB[target]
        return res
