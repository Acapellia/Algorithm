sinput = input()
l = []
sum = 0
for i in range(len(sinput)):
    if sinput[i].isalpha():
        l.append(sinput[i])
    else:
        sum += int(sinput[i])
l.sort()
for x in l:
    print(x, end='')
print(sum)
'''
K1KA5CB7
'''
'''
AJKDLSI412K4JSJ9D
'''