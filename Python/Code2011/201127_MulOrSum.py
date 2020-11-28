strnum = input()
num = []
for i in range(len(strnum)):
    num.append(int(strnum[i]))
print(num)

result = 0
for n in num:
    if (result * n == 0) or (result * n == result):
        result += n
    else:
        result *=n

print(result)
'''
02984
'''
'''
567
'''