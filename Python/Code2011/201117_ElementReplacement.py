n,k = map(int,input().split())
farray = list(map(int,input().split()))
sarray = list(map(int,input().split()))
farray.sort()
sarray.sort(reverse=True)
idx = 0
while idx < k and farray[idx]<sarray[idx]:
    farray[idx], sarray[idx] = sarray[idx], farray[idx]
    idx+=1
print(sum(farray))