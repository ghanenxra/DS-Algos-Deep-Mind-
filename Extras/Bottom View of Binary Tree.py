class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(3)
root.left.right = Node(4)

def bottomView(root):
            if root is None:
                return None
            
            if root.left is not None:
                bottomView(root.left)
                
            if root.left is None and root.right is None:
                print(root.data)

            if root.right is not None:
                bottomView(root.right)
            
            # if root is not None:
            #     bottomView(root.left == None)
            #     print(root.data)
            #     bottomView(root.right == None)
                
                return root

bottomView(root)