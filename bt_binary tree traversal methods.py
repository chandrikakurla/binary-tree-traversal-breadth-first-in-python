class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
# left root right
def print_Inorder(root):
    if root:
        print_Inorder(root.left)
        print(root.data,end=" ")
        print_Inorder(root.right)
    
# root left right
def print_Preorder(root):
    if root:
        print(root.data,end=" ")
        print_Preorder(root.left)
        print_Preorder(root.right)
    
#left right root
def print_Postorder(root):
    if root:
        print_Postorder(root.left)
        print_Postorder(root.right)
        print(root.data,end=" ")
    
if __name__=="__main__":
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    print_Inorder(root)
    print_Preorder(root)
    print_Postorder(root)
    
