class Solution:
    def minMoves2(self, nums: 'List[int]') -> 'int':
        nums.sort()
        mid = len(nums) // 2
        target = nums[mid]
        res = 0
        for num in nums:
            res += abs(target - num)
        return res


if __name__ == "__main__":
    print(Solution().minMoves2([1, 2, 3, 4, 5, 6]))
