class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def dfs(s, left_num, right_num, result):
            if left_num < 0 or right_num < 0 or left_num > right_num:
                return
            if left_num == 0 and right_num == 0:
                result.append(s)
            dfs(s + "(", left_num - 1, right_num, result)
            dfs(s + ")", left_num, right_num - 1, result)

        result = list()
        dfs("", n, n, result)
        return result
