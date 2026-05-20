class CreateList:
    # Represents the node of the list.
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    # This function will add the new node at the end of the list.
    def add(self, data):
        # Create a new node
        new_node = self.Node(data)

        # Checks if the list is empty.
        if self.head is None:
            # If the list is empty, both head and tail would point to the new node.
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            # Tail will point to the new node.
            self.tail.next = new_node
            # New node will become the new tail.
            self.tail = new_node
            # Since it is a circular linked list, the tail will point to the head.
            self.tail.next = self.head

    # Displays all the nodes in the list.
    def display(self):
        current = self.head
        if self.head is None:
            print("List is empty")
        else:
            print("Nodes of the circular linked list:")
            while True:
                # Prints each node by incrementing the pointer.
                print(current.data, end=" ")
                current = current.next
                if current == self.head:
                    break
            print()

    def calculate_sum(self):
        current = self.head
        total = 0
        if self.head is not None:
            while True:
                total += current.data
                current = current.next
                if current == self.head:
                    break
        return total


if __name__ == '__main__':
    cl = CreateList()
    for i in range(1, 10):  # Adding 6 more nodes with user-specified values (total to 3 + 6 = 9)
        data = int(input(f"Enter data for node {i}: "))
        cl.add(data)

    cl.display()  # Displaying all the nodes in the list

    sum_of_integers = cl.calculate_sum()
    print("Sum of Integers:", sum_of_integers)
