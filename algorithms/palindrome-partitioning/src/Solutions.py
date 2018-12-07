class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def is_palindrome(string):
            start = 0
            end = len(string) - 1
            while start < end:
                if string[start] != string[end]:
                    return False
                start += 1
                end -= 1
            return True

        def dfs(string, paths, res):
            if len(string) <= 1:
                if len(string) == 1:
                    paths += [string]
                res.append(paths)
                return
            for i in range(len(string)):
                sub_string = string[:i + 1]
                if (is_palindrome(sub_string)):
                    dfs(string[i + 1:], paths + [sub_string], res)

        res = []
        dfs(s, [], res)
        return res
