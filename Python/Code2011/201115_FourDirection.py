import sys

if __name__ == '__main__':
    n = input()
    dir = list(sys.stdin.readline().rstrip().split())
    x = y = 1
    for d in dir:
        if d == 'U' and y>1:
            y-=1
        elif d == 'D' and y<int(n) :
            y+=1
        elif d == 'L' and x>1:
            x-=1
        elif d == 'R' and x<int(n):
            x+=1
    print(y,x)