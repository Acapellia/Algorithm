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

def setting(data):
    return data[2]
v,e = map(int, input().split())
parent = [0] * (v+1)

for i in range(0,v+1):
    parent[i] = i

result = 0
edges = []

for i in range(e):
    x,y,w = map(int, input().split())
    edges.append((x,y,w))
edges.sort(key = setting)

for e in edges:
    x, y, w = e
    if findParent(parent,x) != findParent(parent,y):
        unionParent(parent,x,y)
        edges.append((x,y,w))
        result += w

print(result - edges[-1][2])


'''
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
'''