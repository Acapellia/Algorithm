n, m = map(int, input().split())
mtype = []
dp = [10001] * (m+1)
dp[0] = 0
for i in range(n):
    mtype.append(int(input()))
def makeMoney(money):
    if money >= m:
        return
    for mt in mtype:
        if money + mt <= m:
            dp[money + mt] = min(dp[money + mt], dp[money] + 1)
            makeMoney(money+mt)
makeMoney(0)
if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
'''
2 15
2
3
'''