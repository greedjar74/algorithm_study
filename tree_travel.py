# 트리 순회

def preorder(a):
    if a <= N:
        print(tree[a], end=' ')
        preorder(a*2)
        preorder(a*2+1)

def inorder(a):
    if a <= N:
        inorder(a*2)
        print(tree[a], end=' ')
        inorder(a*2+1)

def postorder(a):
    if a <= N:
        postorder(a*2)
        postorder(a*2+1)
        print(tree[a], end=' ')

N = 9
tree = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I']
preorder(1)
print()
inorder(1)
print()
postorder(1)