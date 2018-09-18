class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        first_str = strs[0]
        cache = [0 for i in range(len(strs))]
        cache[0] = len(first_str) - 1
        for i in range(1, len(strs)):
            total_flag = True
            target_str = strs[i]
            for j in range(len(target_str)):
                flag = True
                if j < len(first_str):
                    if first_str[j] == target_str[j]:
                        cache[i] = j
                        flag = False
                        total_flag = False
                if flag:
                    break
            if total_flag:
                return ""
        return first_str[:min(cache) + 1]
