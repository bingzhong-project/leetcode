class Solution:
    def numberOfArithmeticSlices(self, A: 'List[int]') -> 'int':
        def number(sub_length):
            return (sub_length - 1) * (sub_length - 2) // 2

        start = 0
        diff = 0
        res = 0
        for end in range(1, len(A)):
            if end - start < 2:
                diff = A[end] - A[start]
            else:
                if A[end] - A[end - 1] != diff:
                    res += number(end - start)
                    start = end - 1
                    diff = A[end] - A[start]
                elif end == len(A) - 1:
                    res += number(end - start + 1)
        return res
