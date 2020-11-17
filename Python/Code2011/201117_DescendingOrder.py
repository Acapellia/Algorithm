n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))
array.sort(reverse=True)
for n in array:
    print(n,end=' ')
