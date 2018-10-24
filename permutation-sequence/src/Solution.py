class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # 该解法超时
        def calculate(n):
            if n <= 2:
                return n
            return n * calculate(n - 1)

        node_count = int(calculate(n) / n)
        div = k // node_count
        mod = k % node_count
        if mod == 0:
            node_num = div
        else:
            node_num = div + 1

        def dfs(nums, level, visited, path, res):
            if len(path) == len(nums):
                res.append(path)
            for i in range(len(nums)):
                if level == 0 and i != node_num - 1:
                    continue
                if i not in visited:
                    dfs(nums, level + 1, visited + [i], path + str(nums[i]),
                        res)

        res = []
        dfs([i for i in range(1, n + 1)], 0, [], "", res)
        return res[k - 1 - node_count * (node_num - 1)]
