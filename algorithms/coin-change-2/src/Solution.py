class Solution:
    def change(self, amount: 'int', coins: 'List[int]') -> 'int':
        def func(amount, coins, index, memo):
            if (index, amount) in memo:
                return memo[(index, amount)]
            if amount == 0:
                return 1
            ways = 0
            for i in range(index, -1, -1):
                if amount >= coins[i]:
                    ways += func(amount - coins[i], coins, i, memo)
            memo[(index, amount)] = ways
            return ways

        return func(amount, coins, len(coins) - 1, {})


if __name__ == "__main__":
    print(Solution().change(5, [1, 2, 5]))
