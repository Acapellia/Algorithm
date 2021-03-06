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

for i in range(1,v+1):
    parent[i] = i

cycle = False

for i in range(e):
    x,y = map(int, input().split())
    if findParent(parent,x) == findParent(parent,y):
        cycle = True
        break
    else:
        unionParent(parent,x,y)

if cycle == True:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")