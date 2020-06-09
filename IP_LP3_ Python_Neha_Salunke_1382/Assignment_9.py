# -*- coding: utf-8 -*-
"""
Created on Sat May 30 17:04:43 2020

@author: Sai
"""

class TreeNode(object):
    def __init__(self, x):
        self.data= x
        self.left = None
        self.right = None

def isBST(root):
    stack = []
    prev = None
    
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if prev and root.data <= prev.data:
            return False
        prev = root
        root = root.right
    return True

root = TreeNode(2)  
root.left = TreeNode(1)  
root.right = TreeNode(3) 
 
result = isBST(root)
print(result)

root = TreeNode(1)  
root.left = TreeNode(2)  
root.right = TreeNode(3) 
 
result = isBST(root)
print(result)
