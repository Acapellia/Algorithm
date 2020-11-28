n = int(input())
person = list(map(int, input().split()))
person.sort()
result = 0
cnt = 0
print("person")
print(person)
for i in range(len(person)):
    cnt += 1
    if person[i] == cnt:
        result += 1
        cnt = 0

print(result)

'''
5
2 3 1 2 2
'''
'''
15
1 2 3 2 4 2 3 1 5 4 3 2 2 3 4
'''