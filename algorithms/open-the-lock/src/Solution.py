class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """

        def get_next_sequence(cur_seq):
            res = []
            for i in range(len(cur_seq)):
                num = int(cur_seq[i])

                up = num + 1
                up = up if up < 10 else 0
                up_seq_list = list(cur_seq)
                up_seq_list[i] = str(up)
                res.append(''.join(up_seq_list))

                down = num - 1
                down = down if down >= 0 else 9
                down_seq_list = list(cur_seq)
                down_seq_list[i] = str(down)
                res.append(''.join(down_seq_list))
            return res

        if '0000' in deadends:
            return -1
        if target in deadends:
            return -1

        distance = {}
        distance['0000'] = 0

        queue = []
        queue.append('0000')

        while len(queue) > 0:
            seq = queue.pop(0)
            for next_seq in get_next_sequence(seq):
                if next_seq in deadends:
                    continue
                if next_seq in distance:
                    continue
                distance[next_seq] = 0
                distance[next_seq] = distance[seq] + 1
                if next_seq == target:
                    return distance[next_seq]
                queue.append(next_seq)

        return -1
