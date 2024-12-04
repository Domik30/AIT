class PriorityQueue:
    def __int__(self):
        self.queue = []

    def push(self, number, priority):
        self.queue.append(priority, number)

    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return Nonequeue
