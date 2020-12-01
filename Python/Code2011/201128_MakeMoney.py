n = int(input())
num = list(map(int,input().split()))
num.sort()
result = 1

for x in num:
    if result < x:
        break
    result += x

print(result)
'''
5
3 2 1 1 9

1 1 2 3 9
'''

