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

        deadends = set(deadends)

        if '0000' in deadends:
            return -1
        if target in deadends:
            return -1

        queue = []
        queue.append('0000')

        layer = 0

        while len(queue) > 0:
            layer += 1
            for _ in range(len(queue)):
                seq = queue.pop(0)
                for next_seq in get_next_sequence(seq):
                    if next_seq in deadends:
                        continue
                    if next_seq == target:
                        return layer
                    queue.append(next_seq)
                    deadends.add(next_seq)

        return -1
