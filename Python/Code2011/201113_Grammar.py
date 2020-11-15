#===========================================================
'''
# 파이썬에서의 부등식
x = 15
if 0 < x < 20:
    print(True)
else :
    print(False)
'''
#===========================================================
'''
# 함수와 람다식
def add(a,b):
    return a+b
print(add(3,4))
print((lambda a,b : a+b)(3,4))
'''
#==========================================================
'''
# input
# 데이터의 개수 입력
n = int(input())
# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))
data.sort(reverse=True)
print(data)
# 공백을 기준으로 구분하여 적은 수의 데이터 입력
n,m,k = map(int, input().split())
print(n,m,k)
'''
#===========================================================
# readline() 예시
# import sys
# data = sys.stdin.readline().rstrip()
# print(data)
# 변수 출력
answer = 7
print("정답은 " + str(answer) + "입니다.")
print("정답은",str(answer),"입니다.")
print(f"정답은 {answer}입니다.")
#=============================================================
