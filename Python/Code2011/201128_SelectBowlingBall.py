'''
n,m = map(int, input().split())
ball = list(map(int,input().split()))

ball.sort()
cnt = 0
for i in range(len(ball)-1):
    for j in range(i+1,len(ball)):
        if ball[i] != ball[j]:
            cnt += 1

print(cnt)
'''
n,m = map(int, input().split())
ball = list(map(int, input().split()))
result = 0
count = [0 for _ in range(m+1)]

for b in ball:
    count[b] += 1

for i in range(1,m+1):
    n -= count[i]
    result += (n * count[i])

print(result)
'''
5 3
1 3 2 3 2

'''
8 5 
1 5 4 3 2 4 5 2
'''