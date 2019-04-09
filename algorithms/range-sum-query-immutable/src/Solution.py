class NumArray:
    def __init__(self, nums: 'List[int]'):
        self.range = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                self.range[i] = nums[i]
            else:
                self.range[i] = self.range[i - 1] + nums[i]

    def sumRange(self, i: 'int', j: 'int') -> 'int':
        if i == 0:
            return self.range[j]
        else:
            return self.range[j] - self.range[i - 1]
