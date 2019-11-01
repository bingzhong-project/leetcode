class Solution:
    def carFleet(self, target: int, position: list, speed: list) -> int:
        car_speed = {}
        car_time = []
        for i in range(len(position)):
            car_speed[position[i]] = speed[i]
        for pos in sorted(position, reverse=True):
            car_time.append((target - pos) / car_speed[pos])
        res = 0
        cur_time = 0
        for time in car_time:
            if cur_time < time:
                cur_time = time
                res += 1

        return res


if __name__ == "__main__":
    print(Solution().carFleet(
        target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]))
