class Queue:
    def __init__(self):
        self.queue = []

    def push(self, number):
        self.queue.append(number)

    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return None


queue = Queue()


queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
queue.push(5)
vyhozene_cislo = queue.pop()

print(vyhozene_cislo)
print(queue.queue)



found_node = linked_list.get_node("B")
print(f"Found node: {found_node.name}")