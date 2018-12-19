class Solution:
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        max_value = "2147483648"

        def dfs(string, paths, limit_factory, res):
            if len(res) > 0:
                return
            if len(string) == 0 and len(paths) >= 3:
                res.extend(paths)
                return
            for i in range(1, len(string) + 1):
                num_str = string[:i]
                if len(max_value) <= len(num_str) and num_str > max_value:
                    break
                if (len(num_str) > 1 and num_str.startswith("0")):
                    break
                num = int(num_str)
                if len(paths) < 2 or num == paths[-1] + paths[-2]:
                    dfs(string[i:], paths + [num], limit_factory - 1, res)

        res = []
        dfs(S, [], 3, res)
        return res
