class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.head
        while current and current.next:
            current = current.next
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    raise IndexError("Position out of range")
                current = current.next
            new_node.prev = current
            new_node.next = current.next
            if current.next:
                current.next.prev = new_node
            current.next = new_node

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

if __name__ == "__main__":
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    print("Original Doubly Linked List (Forward):")
    linked_list.display_forward()

    print("\nOriginal Doubly Linked List (Backward):")
    linked_list.display_backward()

    linked_list.insert(4, 1)
    print("\nDoubly Linked List after inserting 4 at position 1 (Forward):")
    linked_list.display_forward()

    linked_list.delete(2)
    print("\nDoubly Linked List after deleting 2 (Forward):")
    linked_list.display_forward()
