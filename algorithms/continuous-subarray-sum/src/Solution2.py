class Solution:
    def checkSubarraySum(self, nums: 'List[int]', k: 'int') -> 'bool':
        mods = {0: -1}
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            mod = sum if k == 0 else sum % k
            if mod in mods:
                if i - mods[mod] > 1:
                    return True
            else:
                mods[mod] = i
        return False
