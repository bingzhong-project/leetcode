class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        node_nums = [1 for i in range(n)]
        for i in range(1, n):
            node_nums[i] = i * node_nums[i - 1]
        node_nums.sort(reverse=True)

        def dfs(nums, level, n, k, path, res):
            if len(path) == n:
                res.append(path)
                return
            node_count = node_nums[level]
            div = k // node_count
            mod = k % node_count
            if mod == 0:
                node_num = div
            else:
                node_num = div + 1
            for i in range(len(nums)):
                if i != node_num - 1:
                    continue
                tmp = nums[:]
                del tmp[i]
                dfs(tmp, level + 1, n, k - node_count * (node_num - 1),
                    path + str(nums[i]), res)

        res = []
        dfs([i for i in range(1, n + 1)], 0, n, k, "", res)
        return res[-1]
