class Stack:
    def __init__(self, size):
        self.arr = [0] * size
        self.top = -1
        self.capacity = size

    def push(self, x):
        if self.is_full():
            print("Stack Overflow")
            return
        self.top += 1
        self.arr[self.top] = x
        print("Inserting", x)

    def pop(self):
        if self.is_empty():
            print("Stack Empty")
            return
        item = self.arr[self.top]
        self.top -= 1
        return item

    def get_size(self):
        return self.top + 1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def print_stack(self):
        for i in range(self.top + 1):
            print(self.arr[i], end=", ")
        print()

if __name__ == '__main__':
    size = int(input("Enter the size of the stack: "))
    stack = Stack(size)

    while True:
        print("\nMenu:")
        print("1. Push")
        print("2. Pop")
        print("3. Print Stack")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            data = int(input("Enter data to push: "))
            stack.push(data)
        elif choice == '2':
            if stack.is_empty():
                print("Stack is empty. Cannot pop.")
            else:
                popped = stack.pop()
                print("Popped element:", popped)
        elif choice == '3':
            print("Stack: ", end="")
            stack.print_stack()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")