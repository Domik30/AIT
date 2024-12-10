class Node:
    def __init__(self, name=None):
        self.name = name
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_to_the_end(self, new_node):
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def push_behind(self, target_node, new_node):
        current = self.head
        while current:
            if current == target_node:
                new_node.next = current.next
                current.next = new_node
                if current == self.tail:
                    self.tail = new_node
                break
            current = current.next

    def remove(self, node_to_remove):
        current = self.head
        previous = None
        while current:
            if current == node_to_remove:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                if current == self.tail:
                    self.tail = previous
                break
            previous = current
            current = current.next

    def get_node(self, name):
        current = self.head
        while current:
            if current.name == name:
                return current
            current = current.next
        return None

    def len(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def get_first(self):
        return self.head

    def get_last(self):
        return self.tail


node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")

linked_list = LinkedList()
linked_list.push_to_the_end(node1)
linked_list.push_to_the_end(node2)
linked_list.push_to_the_end(node3)


linked_list.push_behind(node2, node4)


linked_list.remove(node3)


print(f"List length: {linked_list.len()}")
print(f"First node: {linked_list.get_first().name}")
print(f"Last node: {linked_list.get_last().name}")