class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        cache = {}
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str not in cache:
                res = list()
                res.append(str)
                cache[sorted_str] = res
            else:
                cache[sorted_str].append(str)
        return list(cache.values())
