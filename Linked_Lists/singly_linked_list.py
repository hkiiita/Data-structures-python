class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


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
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def print_list(self):
        values = []
        pointer = self.head
        while pointer:
            values.append(str(pointer.data))
            pointer = pointer.next
        print("->".join(values))

    def reverse(self):
        previous = None
        current = self.head
        next = current.next

        while next:
            current.next = previous
            previous = current
            current = next
            next = current.next
        current.next = previous
        print("Printing  : ")
        values = []
        tempo = current
        while tempo:
            values.append(str(tempo.data))
            tempo = tempo.next
        print("->".join(values))

        return

    def reverse_store(self):
        store = []
        traveller = self.head
        while traveller:
            store.append(traveller.data)
            traveller = traveller.next

        temp_head = None
        temp_tail = None
        for item in reversed(store):
            if not temp_head:
                temp_head = Node(item)
                temp_tail = temp_head
            else:
                temp_tail.next = Node(item)
                temp_tail = temp_tail.next
        print("Printing  : ")
        values = []
        tempo = temp_head
        while tempo:
            values.append(str(tempo.data))
            tempo = tempo.next
        print("->".join(values))
        return temp_head


singly_linked_list = LinkedList()
singly_linked_list.insert_end(1)
singly_linked_list.insert_end(2)
singly_linked_list.insert_end(3)
singly_linked_list.insert_end(4)

singly_linked_list.print_list()

# singly_linked_list.remove(1)
# singly_linked_list.print_list()

# singly_linked_list.reverse_store()
singly_linked_list.reverse()
# singly_linked_list.print_list()
