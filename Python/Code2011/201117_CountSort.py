array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0] * (max(array)+1)
for n in array:
    count[n]+=1
print(count)
for k in range(len(count)):
    for c in range(count[k]):
        print(k, end = ' ')
