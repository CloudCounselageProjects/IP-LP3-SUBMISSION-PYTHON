
maximum = 4294967296
minimum = -4294967296
class TreeNode: 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None

def isBST(node): 
    return (isBSTUtil(node, minimum, maximum)) 

def isBSTUtil(node, mini, maxi): 
    if node is None: 
        return True
    if node.data < mini or node.data > maxi: 
        return False

    return (isBSTUtil(node.left, mini, node.data -1) and
          isBSTUtil(node.right, node.data+1, maxi)) 

a=int(input('Root Node: '))
b=int(input('Left Node: '))
c=int(input('Right Node: '))
root = TreeNode(a) 
root.left = TreeNode(b) 
root.right = TreeNode(c)

if (isBST(root)): 
    print ("True")
else: 
    print ("False")
    
    
    
    
"""
OUTPUT:
    
case 1:
Root Node: 2

Left Node: 1

Right Node: 3
True

case 2:
Root Node: 1

Left Node: 2

Right Node: 3
False

"""
