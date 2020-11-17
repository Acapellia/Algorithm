import sys
n,m = map(int, input().split())
x,y,dir = map(int,input().split())
visit = [m * [0] for _ in range(n)]
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visit[x][y] = 1

def turn_left():
    global  dir
    dir -= 1
    if dir == -1:
        dir = 3

count = 1
turn_time = 0
while True:
    turn_left()
    tx = x + dx[dir]
    ty = y + dy[dir]
    if(visit[tx][ty] == 0 and array[tx][ty] == 0):
        visit[tx][ty] = 1
        x = tx
        y = ty
        count+=1
        turn_time = 0
        continue
    else:
        turn_time +=1

    if turn_time == 4:
        tx = x - dx[dir]
        ty = y - dy[dir]
        if array[tx][ty] == 0:
            x = tx
            y = ty
        else:
            break
        turn_time = 0
print(count)
'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''