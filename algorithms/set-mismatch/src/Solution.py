class Solution:
    def findErrorNums(self, nums: 'List[int]') -> 'List[int]':
        nums_set = set()
        n = len(nums)
        for i in range(1, n + 1):
            nums_set.add(i)
        duplicate = None
        for num in nums:
            if num in nums_set:
                nums_set.remove(num)
            else:
                duplicate = num

        return [duplicate, list(nums_set)[0]]


if __name__ == "__main__":
    print(Solution().findErrorNums([1, 2, 2, 4]))
