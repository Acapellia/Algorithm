import sys
from bisect import  bisect_left
n = int(input())
apart = list(map(int,sys.stdin.readline().rstrip().split()))
m = int(input())
fpart = list(map(int,sys.stdin.readline().rstrip().split()))
apart.sort()
def binarySearch(array,x):
    idx = bisect_left(array,x)
    if idx != len(array) and array[idx] == x:
        return idx
    else:
        return -1
for fp in fpart:
    if  binarySearch(apart,fp) == -1:
        print('no', end = ' ')
    else:
        print('yes', end = ' ')

'''
5
8 3 7 9 2
3
5 7 9
'''