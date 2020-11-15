# 이것이 코딩테스드다 with 파이썬 - 99p, 1이 될 때까지
# 그리디 알고리즘
import sys
if __name__ == '__main__':
    n,k = map(int, sys.stdin.readline().rstrip().split())
    cnt = 0
    while n != 1:
        if n % k == 0:
            n /= k
        else:
            n-=1
        cnt += 1
    print(cnt)
