num = input()
one = 0
zero = 0
if num[0] == '0':
    zero += 1
else:
    one +=1

for i in range (1,len(num)):
    if num[i-1] != num[i]:
        if num[i] == zero:
            zero += 1
        else:
            one += 1

print(min(one,zero))
'''
0001100
'''