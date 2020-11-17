INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]
for d in range(1,n+1):
    graph[d][d] = 0
for _ in range(m):
    x,y,w = map(int, input().split())
    graph[x][y] = w
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print('INF', end = ' ')
        else:
            print(graph[i][j], end = ' ')
    print()

'''
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2 
'''