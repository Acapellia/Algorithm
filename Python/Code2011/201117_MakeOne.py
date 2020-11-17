n = int(input())
dp = [30001] * (n+1)
dp[n] = 0
divide = [5,3,2]

def makeOne(num):
    if num == 1:
        return
    for d in divide:
        t = num % d
        n = num // d
        if t == 0:
            dp[n] = min(dp[n], dp[num] + 1)
            makeOne(n)
    n = num - 1
    dp[n] = min(dp[n], dp[num] + 1)
    makeOne(num-1)

makeOne(n)
print(dp[1])

