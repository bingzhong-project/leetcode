class Solution:
    def matrixReshape(self, nums: 'List[List[int]]', r: 'int',
                      c: 'int') -> 'List[List[int]]':
        size = 0
        for i in range(len(nums)):
            size += len(nums[i])
        if size == r * c:
            matrix = []
            array = []
            for i in range(len(nums)):
                for j in range(len(nums[i])):
                    array.append(nums[i][j])
                    if len(array) == c:
                        matrix.append(array[::])
                        array = []
            return matrix
        else:
            return nums[::]
