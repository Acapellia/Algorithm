def findParent(parent,x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

def unionParent(parent,a,b):
    a = findParent(parent,a)
    b = findParent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int, input().split())
parent = [0] * (v+1)

for i in range(0,v+1):
    parent[i] = i

cycle = False

for i in range(e):
    x,y, op = map(int, input().split())
    if op == 0:
        unionParent(parent,x,y)
    elif op == 1:
        if findParent(parent, x) == findParent(parent, y):
            print('YES')
        else:
            print('NO')

'''
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
'''