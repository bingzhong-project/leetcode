class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def findNSum(nums, target, N, result, results):
            if N == 2:
                left = 0
                right = len(nums) - 1
                while left < right:
                    two_sum = nums[left] + nums[right]
                    if target == two_sum:
                        results.append(result + [nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif target < two_sum:
                        right -= 1
                    else:
                        left += 1
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
