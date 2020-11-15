# 이것이 코딩테스드다 with 파이썬 - 96p, 숫자 카드 게임
# 그리디 알고리즘
import sys
if __name__ == '__main__':
    n,m = map(int, sys.stdin.readline().rstrip().split())
    result = 0
    for i in range(0,n):
        array = list(map(int, sys.stdin.readline().rstrip().split()))
        min_value = min(array)
        if result < min_value:
            result = min_value
    print(result)
