class DoublyLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = self.Node(data)

        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("previous node cannot be None")
            return

        new_node = self.Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    def insert_end(self, data):
        new_node = self.Node(data)

        temp = self.head

        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def delete_node(self, del_node):
        if self.head is None or del_node is None:
            return

        if self.head == del_node:
            self.head = del_node.next

        if del_node.next is not None:
            del_node.next.prev = del_node.prev

        if del_node.prev is not None:
            del_node.prev.next = del_node.next

    def print_list(self, node):
        last = None
        while node is not None:
            print(node.data, end="->")
            last = node
            node = node.next
        print()

if __name__ == "__main__":
    doubly_ll = DoublyLinkedList()

    doubly_ll.insert_end(5)
    doubly_ll.insert_front(1)
    doubly_ll.insert_front(6)
    doubly_ll.insert_end(9)

    # insert 11 after head
    doubly_ll.insert_after(doubly_ll.head, 11)

    # insert 15 after the second node
    doubly_ll.insert_after(doubly_ll.head.next, 15)

    # Add 5 more nodes to the linked list
    doubly_ll.insert_end(22)
    doubly_ll.insert_end(33)
    doubly_ll.insert_end(44)
    doubly_ll.insert_end(55)
    doubly_ll.insert_end(66)

    doubly_ll.print_list(doubly_ll.head)

    # delete the last node
    doubly_ll.delete_node(doubly_ll.head.next.next.next.next.next)

    doubly_ll.print_list(doubly_ll.head)
