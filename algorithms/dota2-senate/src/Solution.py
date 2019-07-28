class Solution:
    def predictPartyVictory(self, senate: 'str') -> 'str':
        r_queue = []
        d_queue = []
        for i in range(len(senate)):
            r_queue.append(i) if senate[i] == 'R' else d_queue.append(i)
        while r_queue and d_queue:
            r = r_queue.pop(0)
            d = d_queue.pop(0)
            r_queue.append(r + len(senate)) if r < d else d_queue.append(
                d + len(senate))
        return 'Dire' if len(d_queue) > 0 else 'Radiant'
