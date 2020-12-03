num = input()
lsum = rsum = 0
length = len(num)
for i in range(0,int(length/2)):
    lsum += int(num[i])
for i in range(int(length/2),length):
    rsum += int(num[i])
if lsum == rsum:
    print('LUCKY')
else:
    print('READY')
'''
123402
'''