class Solution:
    def nextGreaterElement(self, n: 'int') -> 'int':
        nums = []
        div = n
        while div > 0:
            div, mod = divmod(div, 10)
            nums.append(mod)
        nums = nums[::-1]

        index = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                index = i - 1
                break
        if index < 0:
            return -1
        for j in range(len(nums) - 1, index, -1):
            if nums[j] > nums[index]:
                temp = nums[j]
                nums[j] = nums[index]
                nums[index] = temp
                break
        nums = nums[:index + 1] + sorted(nums[index + 1:])

        res = 0

        for num in nums:
            res = res * 10 + num

        return res if res < 2**31 else -1
