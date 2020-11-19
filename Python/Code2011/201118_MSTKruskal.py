def findParent(parent,x):
    if parent[x] != x:
        parent[x] = findParent(parent,parent[x])
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

edges = []
result = 0

for i in range(1,v+1):
    parent[i] = i

for _ in range(e):
    x,y,w = map(int, input().split())
    edges.append((x,y,w))

edges.sort(key = setting)

for edge in edges:
    x, y, w = edge
    if findParent(parent,x) == findParent(parent,y):
        continue
    unionParent(parent,x,y)
    result += w

print(result)

'''
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
'''
