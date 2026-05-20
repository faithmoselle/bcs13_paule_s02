'''Programmed by: Faith Paule
Menu Driven
CREATE A FUNCTIONAL PYTHON PROGRAM FOR THE FOLLOWING SPECIFICATIONS:
Implement a MENU-DRIVEN code of the following options:
LISTS
LINKED LISTS
STACKS
QUEUES
TREES
QUIT
'''


class Menu:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def preorder(node):
    if node:
        print(node.key, end=" ")
        preorder(node.left)
        preorder(node.right)


def inorder(node):
    if node:
        inorder(node.left)
        print(node.key, end=" ")
        inorder(node.right)


def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.key, end=" ")


def leavecount(node):
    if not node:
        return 0
    if not node.left and not node.right:
        return 1
    return leavecount(node.left) + leavecount(node.right)


while True:
    print("Dashboard Menu")
    print("[1] - LIST")
    print("[2] - LINKED LISTS")
    print("[3] - STACKS")
    print("[4] - QUEUES")
    print("[5] - TREES")
    print("[6] - EXIT - DONE")

    option = int(input('Choose a Operation (1-6): '))

    if option == 1:  # Operation: List
        print("\nLIST Selected.")
        items = [0] * 10
        print("Enter array size from 1-10: ")
        arr = int(input())

        print("\nEnter array elements: ")
        for i in range(arr):
            items[i] = int(input())

        print("\nEnter the element to search: ")
        target = int(input())

        found = False
        for i in range(arr):
            if items[i] == target:
                print(target, 'found at position', i + 1, "\n")
                found = True
                break
        if not found:
            print("\n", target, "not found\n")

    elif option == 2:  # Operation: Linked List
        print("\nLINKED LIST Selected.")
        print("This is an example of a CIRCULAR LINKED LIST\n")


        class Directory:
            class Node:
                def __init__(self, data):
                    self.data = data
                    self.next = None

            def __init__(self):
                self.head = None
                self.tail = None

            def add(self, data):
                new_node = self.Node(data)
                if self.head is None:
                    self.head = new_node
                    self.tail = new_node
                    new_node.next = self.head
                else:
                    self.tail.next = new_node
                    self.tail = new_node
                    self.tail.next = self.head

            def display(self):
                current = self.head
                if self.head is None:
                    print("Empty! Input valid input please.")
                else:
                    print("The nodes are:")
                    while True:
                        print(current.data, end=" ")
                        current = current.next
                        if current == self.head:
                            break
                    print()

            def total(self):
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
            cd = Directory()
            for i in range(1, 10):
                data = int(input(f"The inputs are {i}: "))
                cd.add(data)
            cd.display()
            total = cd.total()
            print("The total is:", total)

        print()

    elif option == 3:  # This is the code for Stacks
        print("\nSTACKS Selected.")


        class Stack:
            def __init__(self, size):
                self.arr = [0] * size
                self.capacity = size
                self.top = -1

            def push(self, x):
                if self.is_full():
                    print("Overflow!")
                    SystemExit
                print("Inputting: {x}")
                self.top += 1
                self.arr[self.top] = x

            def pop(self):
                if self.is_empty():
                    print("The stack do not contain any inputs.")
                    SystemExit
                popped = self.arr[self.top]
                self.top -= 1
                return popped

            def get_size(self):
                return self.top + 1

            def is_empty(self):
                return self.top == -1

            def is_full(self):
                return self.top == self.capacity - 1

            def print_stack(self):
                if self.is_empty():
                    print("You did not have any input, please re-enter inputs.")
                    SystemExit
                for i in range(self.top + 1):
                    print(self.arr[i], end=" ")
                print()


        stack = Stack(5)
        option = 0
        while option != 4:

            print("MODES!!!")
            print("[ 1 ] - Push")
            print("[ 2 ] - Pop")
            print("[ 3 ] - Print")
            print("[ 4 ] - Exit")

            option = int(input('Option: '))

            if option == 1:

                stack.push(1)
                stack.push(2)
                stack.push(3)

                print()

            elif option == 2:
                stack.pop()
                print("Popped out: ")
                stack.print_stack()

                print()

            elif option == 3:
                print("Stack: ")
                stack.print_stack()
                print()

            elif option == 4:
                print("Executing the code: ")
                SystemExit
            else:
                print('INVALID INPUT')
                print()
        print()

    elif option == 4:  # This is the code for Queues
        print("\nQUEUES Selected.")
        print("Type 'done' to stop queueing")


        class Queue:
            def __init__(self):
                self.items = []

            def is_empty(self):
                return len(self.items) == 0

            def enqueue(self, item):
                self.items.append(item)

            def dequeue(self):
                if not self.is_empty():
                    return self.items.pop(0)
                else:
                    print("EMPTY!!!")
                    return None

            def size(self):
                return len(self.items)


        queue = Queue()

        while True:
            user_input = input("Queueing... ")

            if user_input.lower() == 'done':
                break

            try:
                element = int(user_input)
                queue.enqueue(element)
            except ValueError:
                print("Invalid input. Please enter an integer.")

        print("\nYou have queued", queue.size(), "elements")

        while not queue.is_empty():
            print("Now, removing from the queue: ", queue.dequeue())

        print("\nIs Queue Empty:", queue.is_empty())
        print()

    elif option == 5:  # This is the code for Trees
        print("\nYou have chosen TREES.")
        root = Menu("F")
        root.left = Menu("A")
        root.right = Menu("I")
        root.left.left = Menu("T")
        root.left.right = Menu("H")
        root.right.left = Menu("P")
        root.right.right = Menu(".")

        print("Traversals: ")
        print("\nPreorder: ")
        preorder(root)
        print("\nInorder: ")
        inorder(root)
        print("\nPostorder: ")
        postorder(root)

        count = leavecount(root)
        print("\nNumber of leaves: ", count, "\n")

    elif option == 6:  # Exit

        print("The program will now close.")
        break

    else:
        print("Invalid choice. Option must be between 1 to 6. Try again.")
        print()