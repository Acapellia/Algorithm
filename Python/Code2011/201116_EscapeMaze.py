from collections import deque
def escapeMaze(arr,x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <0 or nx>=n or ny<0 or ny>=m:
                continue
            if arr[nx][ny] == 0:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx, ny))
    return arr[n-1][m-1]

n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input())))
print(arr)
dx = [-1,0,1,0]
dy = [0,-1,0,1]
result = escapeMaze(arr,0,0)
print(result)

'''
5 6
101010
111111
000001
111111
111111
'''