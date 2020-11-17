def findIce(arr, i, j):
    if (i<0 or i>=n) or (j<0 or j>=m):
        return False
    if arr[i][j] == 0:
        arr[i][j] = 1
        findIce(arr,i-1,j)
        findIce(arr,i+1,j)
        findIce(arr,i,j-1)
        findIce(arr,i,j+1)
        return True
    return False

n,m = map(int, input().split())
arr = []
result = 0

for i in range(0,n):
    arr.append(list(map(int, input())))

for i in range(n):
    for j in range(0,m):
        if findIce(arr,i,j):
            result += 1
print(result)
'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''