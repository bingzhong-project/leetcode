class Solution:
    def fairCandySwap(self, A: list, B: list) -> list:
        A_sum = sum(A)
        B_sum = sum(B)

        choose = set(B)
        res = [0, 0]
        for num in A:
            A_new_sum = A_sum - num
            B_new_sum = B_sum + num
            if A_new_sum > B_new_sum:
                continue
            diff = B_new_sum - A_new_sum
            if diff < 1 or diff % 2 != 0:
                continue
            B_change = diff // 2
            if B_change in choose:
                res = [num, B_change]
                break

        return res
