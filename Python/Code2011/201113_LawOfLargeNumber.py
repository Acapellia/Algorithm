# 이것이 코딩테스드다 with 파이썬 - 92p, 큰 수의 법칙
# 그리디 알고리즘
import sys
def CalcLargeValue(num,n,m,k):
    print(num,n,m,k)
    num.sort(reverse=True)
    print(num)
    max_second = int(m / (k+1))
    max_first = (max_second) * k + m % (k+1)
    result = max_first * num[0] + max_second * num[1]
    return result

if __name__ == '__main__':
    n,m,k = map(int,sys.stdin.readline().rstrip().split())
    num = list(map(int, sys.stdin.readline().rstrip().split()))
    result = CalcLargeValue(num,n,m,k)
    print(result)
