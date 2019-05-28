class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def findNSum(nums, target, N, result, results):
            if N == 2:
                cache = {}
                visited = set()
                for i in range(len(nums)):
                    diff = target - nums[i]
                    if diff in cache and diff not in visited and nums[i] not in visited:
                        results.append(result + [nums[i], diff])
                        visited.add(diff)
                        visited.add(nums[i])
                    cache[nums[i]] = i
            else:
                for i in range((len(nums) - N + 1)):
                    if nums[i] * N > target or nums[-1] * N < target:
                        break
                    if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                        findNSum(nums[i + 1:], target - nums[i], N - 1,
                                 result + [nums[i]], results)

        nums = sorted(nums)
        results = []
        findNSum(nums, target, 4, [], results)

        return results
