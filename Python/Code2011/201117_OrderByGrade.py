n = int(input())
array = []
def setting(data):
    return data[1]
for _ in range(n):
    data = input().split()
    array.append((data[0],int(data[1])))
array = sorted(array, key  = setting)
# array = sorted(array, key = lambda student : student[1])
for s in array:
    print(s[0])