class ReIterator:

    def __init__(self, data):
        self.data = data

    def __iter__(self):
        self.current_value = 0
        return self

    def __next__(self):
        if self.current_value +1 <= len(self.data):
            self.current_value += 1
            return self.data[-self.current_value]
        else:
            raise StopIteration


x = ReIterator([1, 2, 3, 4])
for i in x:
    print(i)
# 4
# 3
# 2
# 1