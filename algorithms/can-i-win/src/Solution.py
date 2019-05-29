class Solution:
    def canIWin(self, maxChoosableInteger: 'int',
                desiredTotal: 'int') -> 'bool':
        def win(length, target, used=0, cache={}):
            if used in cache:
                return cache[used]
            ans = False
            for i in range(1, length + 1):
                cur = 1 << i
                if cur & used == 0:
                    if target - i <= 0 or not win(length, target - i,
                                                  used | cur, cache):
                        ans = True
                        break

            cache[used] = ans
            return ans

        if maxChoosableInteger * (maxChoosableInteger + 1) / 2 < desiredTotal:
            return False
        return win(maxChoosableInteger, desiredTotal)
