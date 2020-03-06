class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        count = 1
        while self.stack and self.stack[-1][0] <= price:
            last_price, last_count = self.stack.pop()
            count += last_count
        self.stack.append((price, count))
        return count
