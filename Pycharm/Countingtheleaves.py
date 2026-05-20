class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def leafCount(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    else:
        return leafCount(node.left) + leafCount(node.right)


if __name__ == '__main__':
    root = Node('p')

    root.left = Node('g')
    root.left.left = Node('c')
    root.left.left.left = Node('a')
    root.left.left.right = Node('e')
    root.left.right = Node('k')
    root.left.right.left = Node('i')
    root.left.right.right = Node('m')

    root.right = Node('w')
    root.right.left = Node('s')
    root.right.left.left = Node('q')
    root.right.left.right = Node('u')
    root.right.right = Node('y')
    root.right.right.left = Node('x')
    root.right.right.right = Node('z')

    print("Total Leaf Nodes = %d" % (leafCount(root)))

print("\nProgrammed by: Faith Paule")
