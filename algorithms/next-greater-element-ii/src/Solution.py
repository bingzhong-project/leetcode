class Solution:
    def nextGreaterElements(self, nums: 'List[int]') -> 'List[int]':
        res = [-1 for _ in range(len(nums))]
        stack = []
        for i in range(2 * len(nums)):
            cursor = i % len(nums)
            while stack and nums[cursor] > nums[stack[-1]]:
                res[stack.pop()] = nums[cursor]
            stack.append(cursor)
        return res
