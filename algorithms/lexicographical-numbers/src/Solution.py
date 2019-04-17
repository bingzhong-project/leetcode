class Solution:
    def lexicalOrder(self, n: 'int') -> 'List[int]':
        def helper(num, n, res):
            if num > n:
                return
            res.append(num)
            index = len(res) - 1
            num *= 10
            while num <= n:
                res.append(num)
                num *= 10
            for i in range(len(res) - 1, index, -1):
                for j in range(1, 10):
                    helper(res[i] + j, n, res)

        res = []
        for i in range(1, 10):
            helper(i, n, res)
        return res
