#Write a Python program to check whether a given a binary tree is a valid binary search tree (BST) or not.  
class newNode:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

def isBST(root,l=None,r=None):
    if (root == None):
        return True
    if (l != None and root.data<=l.data):
        return False
    if (r != None and root.data >= r.data) : 
        return False 
    return isBST(root.left, l, root) and \
        isBST(root.right, root, r)  


root = newNode(2)  
root.left = newNode(1)  
root.right = newNode(3)     
if (isBST(root,None,None)): 
    print("True") 
else: 
    print("False")      

root = newNode(1)  
root.left = newNode(2)  
root.right = newNode(3)     
if (isBST(root,None,None)): 
    print("True") 
else: 
    print("False")      

# Expected output: True 
# Expected output: False 
