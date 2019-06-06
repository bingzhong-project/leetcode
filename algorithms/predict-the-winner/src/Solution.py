class Solution:
    def PredictTheWinner(self, nums: 'List[int]') -> 'bool':
        def game(nums, start, end, player, cache, unused):
            if start == end:
                return nums[start]
            if unused in cache:
                return cache[unused]
            if player > 0:
                res = max(nums[start] +
                          game(nums, start + 1, end, -player, cache, unused -
                               (1 << start)), nums[end] +
                          game(nums, start, end - 1, -player, cache, unused -
                               (1 << end)))
            else:
                res = min(
                    game(nums, start + 1, end, -player, cache,
                         unused - (1 << start)),
                    game(nums, start, end - 1, -player, cache,
                         unused - (1 << end)))
            cache[unused] = res
            return res

        unused = 0
        for i in range(len(nums)):
            unused |= (1 << i)
        res = game(nums, 0, len(nums) - 1, 1, {}, unused)
        return res >= sum(nums) - res
