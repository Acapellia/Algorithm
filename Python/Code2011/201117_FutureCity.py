INF = int(1e9)
n,m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]
for d in range(1,n+1):
    graph[d][d] = 0
for _ in range(m):
    x,y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1
x,k = map(int, input().split())
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])

if graph[1][k] == INF or graph[k][x] == INF:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])

'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
'''
'''
4 2
1 3
2 4
3 4
'''