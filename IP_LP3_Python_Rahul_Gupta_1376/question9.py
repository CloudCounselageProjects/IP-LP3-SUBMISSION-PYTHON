class Tree(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_BST(root):
    stack = []
    prev = None

    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if prev and root.val <= prev.val:
            return False
        prev = root
        root = root.right
    return True


root = Tree(2)
root.left = Tree(1)
root.right = Tree(3)

result = is_BST(root)
print(result)

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)

result = is_BST(root)
print(result)