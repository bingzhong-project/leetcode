class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def is_valid(s):
            if s[0] == '0':
                return s == '0'
            num = int(s)
            return num > 0 and num <= 255

        def is_continue(s, count):
            return 4 - count <= len(s) <= 12 - count

        def dfs(s, ip, count, res):
            if count == 3 and is_valid(s):
                res.append(ip + s)
                return
            i = 1
            while i < 4 and i < len(s):
                temp = s[:i]
                if is_valid(temp) and is_continue(s[i:], count + 1):
                    dfs(s[i:], ip + temp + '.', count + 1, res)
                i += 1

        if len(s) < 4 or len(s) > 12:
            return []
        res = []
        dfs(s, '', 0, res)
        return res
