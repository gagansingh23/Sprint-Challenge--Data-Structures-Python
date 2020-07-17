class RingBuffer:
    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity
        self.position = 0 

    def append(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            self.items[self.position] = item
            self.position += 1

        if self.position == self.capacity:
            self.position = 0

    def get(self):
        return self.items