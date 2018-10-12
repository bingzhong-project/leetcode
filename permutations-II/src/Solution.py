class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(array, visited, result, results):
            if len(result) == len(array) and result not in results:
                results.append(result)
            else:
                for i in range(len(array)):
                    if not visited[i]:
                        if i > 0 and array[i] == array[i - 1] and visited[i
                                                                          - 1]:
                            continue
                        visited[i] = True
                        dfs(array, visited, result + [array[i]], results)
                        visited[i] = False

        results = list()
        dfs(sorted(nums), [False for _ in range(len(nums))], [], results)
        return results
