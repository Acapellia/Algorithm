from  collections import deque

v,e = map(int, input().split())
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]

for _ in range(e):
    x, y = map(int, input().split())
    graph[x].append(y)
    indegree[y] += 1

def topologySort():
    result = []
    q = deque()
    global  v
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for v in graph[now]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    for t in result:
        print(t, end = ' ')

topologySort()

'''
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
'''

