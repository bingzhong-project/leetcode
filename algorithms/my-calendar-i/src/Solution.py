class MyCalendar:
    def __init__(self):
        self.table = []

    def book(self, start: int, end: int) -> bool:
        for i in range(len(self.table)):
            calendar_start = self.table[i][0]
            calendar_end = self.table[i][1]
            if start < calendar_end and end > calendar_start:
                return False
        self.table.append([start, end])
        return True
