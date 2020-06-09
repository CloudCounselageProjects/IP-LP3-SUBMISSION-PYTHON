# taking node values in list such that left node is at odd position , right node is at even position and root is at 0
bst = [int(input()), int(input()), int(input())]  # root,left,right
if bst[0] > bst[1] and bst[0] < bst[2]:
    print(True)
else:
    print(False)
