class Solution:
    def numSubarrayBoundedMax(self, A: list, L: int, R: int) -> int:
        res = 0
        for i in range(len(A)):
            if A[i] >= L and A[i] <= R:
                left = i
                right = i
                while left > 0 and A[i] >= A[left]:
                    left -= 1
                while right < len(A) - 1 and A[i] <= A[right]:
                    right += 1
                if left == right:
                    res += 1
                elif left < i and right > i:
                    left_num = (i - left + 1)
                    right_num = (right - i + 1)
                    res += left_num * right_num
                elif left == i and right > i:
                    res += right - i + 1
                elif left < i and right == i:
                    res += i - left + 1

        return res
