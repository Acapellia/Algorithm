def findParent(parent,x):
    if parent[x] != x:
        return findParent(parent,parent[x])
    return parent[x]
def unionParent(parent,x,y):
    x = findParent(parent,x)
    y = findParent(parent,y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

v, e = map(int, input().split())
parent = [0] * (v+1)
for i in range(1,v+1):
    parent[i] = i
for i in range(e):
    x,y = map(int, input().split())
    unionParent(parent,x,y)

print('각 원소가 속한 집합 : ', end = '')
for i in range(1,v+1):
    print(findParent(parent,i), end = ' ')
print()

print('부모 테이블 : ', end = '')
for i in range(1, v+1):
    print(parent[i],end = ' ')

'''
6 4
1 4
2 3
2 4
5 6
'''