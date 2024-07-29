class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def remove(self, index):
        if index == 1:
            self.head = self.head.next
            return
        count = 1
        current = self.head
        previous = None
        while current and count != index:
            previous = current
            current = current.next
            count = count + 1
        if count == index:
            previous.next = current.next

    def insert_end(self, value):
        new_node = Node()
        new_node.data = value
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def print_list(self):
        values = []
        pointer = self.head
        while pointer:
            values.append(str(pointer.data))
            pointer = pointer.next
        print("->".join(values))


class Node:
    def __init__(self):
        self.data = None
        self.next = None


singly_linked_list = LinkedList()
singly_linked_list.insert_end(1)
singly_linked_list.insert_end(2)
singly_linked_list.insert_end(3)
singly_linked_list.insert_end(4)

singly_linked_list.print_list()

singly_linked_list.remove(1)
singly_linked_list.print_list()
