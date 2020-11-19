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

'''
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
'''