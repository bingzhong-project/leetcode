class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        cache = {}
        for i in range(len(numbers) - 1, -1, -1):
            if numbers[i] in cache:
                return [i + 1, cache[numbers[i]] + 1]
            diff = target - numbers[i]
            cache[diff] = i
