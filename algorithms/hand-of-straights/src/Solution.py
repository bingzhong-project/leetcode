import collections


class Solution:
    def isNStraightHand(self, hand: list, W: int) -> bool:
        if len(hand) % W != 0:
            return False
        counter = collections.Counter(hand)
        hand.sort()
        for num in hand:
            if counter[num] != 0:
                for next_num in range(num, num + W):
                    if next_num not in counter or counter[next_num] == 0:
                        return False
                    else:
                        counter[next_num] -= 1
        return True
