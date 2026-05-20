class Node:
   def __init__(self, key):
      self.leftChild = None
      self.rightChild = None
      self.data = key

# Create a function to perform postorder tree traversal
def PreorderTraversal(root):
   if root:
      print(root.data)
      PreorderTraversal(root.leftChild)
      PreorderTraversal(root.rightChild)

# Main class
if __name__ == "__main__":
   root = Node(1)
   root.leftChild = Node(12)
   root.rightChild = Node(9)
   root.leftChild.leftChild = Node(5)
   root.leftChild.rightChild = Node(6)
   print("\nPreorder traversal of binary tree is")
   PreorderTraversal(root)