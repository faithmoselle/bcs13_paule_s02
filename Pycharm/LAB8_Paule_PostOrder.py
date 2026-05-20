class Node:
   def __init__(self, key):
      self.leftChild = None
      self.rightChild = None
      self.data = key

# Create a function to perform preorder tree traversal
def PostorderTraversal(root):
   if root:
      PostorderTraversal(root.leftChild)
      PostorderTraversal(root.rightChild)
      print(root.data)

# Main class
if __name__ == "__main__":
   root = Node(1)
   root.leftChild = Node(12)
   root.rightChild = Node(9)
   root.leftChild.leftChild = Node(5)
   root.leftChild.rightChild = Node(6)
   print("\nPostorder traversal of binary tree is")
   PostorderTraversal(root)