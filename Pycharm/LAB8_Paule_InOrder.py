class Node:
   def __init__(self, key):
      self.leftChild = None
      self.rightChild = None
      self.data = key

# Create a function to perform inorder tree traversal
def InorderTraversal(root):
   if root:
      InorderTraversal(root.leftChild)
      print(root.data)
      InorderTraversal(root.rightChild)

# Main class
if __name__ == "__main__":
   root = Node(1)
   root.leftChild = Node(12)
   root.rightChild = Node(9)
   root.leftChild.leftChild = Node(5)
   root.leftChild.rightChild = Node(6)

   # Function call
   print("\nInorder traversal of binary tree is")
   InorderTraversal(root)