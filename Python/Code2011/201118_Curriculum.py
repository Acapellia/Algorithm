from collections import deque
import copy
n = int(input())
time = [0] * (n+1)
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for i in range(1, n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for d in data[1:-1]:
        graph[d].append(i)
        indegree[i] += 1

q = deque()
result = copy.deepcopy(time)
for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)

print("graph")
print(graph)
print("--------")
print("indegree")
for i in range(1, n+1):
    print(indegree[i])
print("--------")
while q:
    temp = q.popleft()
    print(f"{temp}'s connected")
    for x in graph[temp]:
        print(x)
        result[x] = max(result[temp]+time[x], result[x])
        indegree[x] -= 1
        if indegree[x] == 0:
            q.append(x)
    print("----------")

for i in range(1, n+1):
    print(result[i])

'''
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
'''