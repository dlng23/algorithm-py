import sys
T = int(sys.stdin.readline())

results = []

for j in range(T):
    n = int(sys.stdin.readline())
    preorder = list(map(int, sys.stdin.readline().split()))
    inorder = list(map(int, sys.stdin.readline().split()))
    
    result = []

    def postorder(po, io):
        if not po:
            return
        
        root = po[0]
        i = io.index(root)

        lp = po[1:1+i]
        li = io[:i]

        rp = po[1+i:]
        ri = io[i+1:]

        postorder(lp, li)
        postorder(rp, ri)
        result.append(root)
    
    postorder(preorder, inorder)
    
    results.append(' '.join(map(str, result)))

print('\n'.join(results))