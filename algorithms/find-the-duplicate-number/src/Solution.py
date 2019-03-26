class Solution:
    def findDuplicate(self, nums: 'List[int]') -> 'int':
        low = 1
        high = len(nums)
        while low < high:
            mid = (low + high) // 2
            less = 0
            greater = 0
            for n in nums:
                if n >= low and n <= high:
                    if n <= mid:
                        less += 1
                    else:
                        greater += 1
            if less > mid - low + 1:
                high = mid
            else:
                low = mid + 1
        return low
