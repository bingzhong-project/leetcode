class Solution:
    def numSubarrayProductLessThanK(self, nums: list, k: int) -> int:
        if k <= 0:
            return 0
        res = 0
        left = 0
        product = 1
        for right in range(len(nums)):
            product *= nums[right]
            while product >= k and left <= right:
                product /= nums[left]
                left += 1
            res += (right - left + 1)
        return res


if __name__ == "__main__":
    print(Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100))
