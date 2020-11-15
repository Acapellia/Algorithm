#================================================
# 내장 함수
# 원소의 합 구하기
result = sum([1,2,3,4,5])
print(result)
# 가장 작은 수, 가장 큰 수 구하기
result = min(7,3,5,2)
print(result)
result = max(7,3,5,2)
print(result)
# 문자열 형태의 계산식 계산
result = eval("(3+5) * 7")
print(result)
# 오름차순, 내림차순
result = sorted([9,1,8,5,4])
print(result)
result = sorted([9,1,8,5,4], reverse=True)
print(result)
# 딕셔너리 value값을 기준으로 정렬하기
result = sorted([('홍길동',35),('이순신',75),('아무개',50)], key = lambda x: x[1],reverse = True)
print(result)
# 리스트 자료형 정렬
data = [9,1,8,5,4]
data.sort()
print(data)
#============================================================
# itertools
# permutations
from itertools import permutations
data = ['A','B','C']
result = list(permutations(data,2))
print(result)
# combinations
from itertools import  combinations
data = ['A','B','C']
result = list(combinations(data,2))
print(result)
# product
from itertools import product
data = ['A','B','C']
result = list(product(data, repeat = 2))
print(result)
# combinations with replacement
from itertools import combinations_with_replacement
data = ['A','B','C']
result = list(combinations_with_replacement(data,2))
print(result)
#==============================================================
# heapq
# 최소힙
import heapq
def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h,value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result
result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
# 최대힙
def heapsort2(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h,-value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result
result = heapsort2([1,3,5,7,9,2,4,6,8,0])
print(result)
#======================================================
# bisect
# 이진 탐색
from bisect import bisect_left, bisect_right
a = [1,2,4,4,8]
x = 4
print(bisect_left(a,x))
print(bisect_right(a,x))
# bisect를 사용하여 특정 범위에 속하는 값의 개수 구하기
def count_by_range(a,left_value,right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)
    return right_index - left_index

a = [1,2,3,3,3,3,4,4,8,9]
# 값이 4인 데이터의 개수
print(count_by_range(a,4,4))
# 값이 [-1,3] 범위에 있는 데이터의 개수
print(count_by_range(a,-1,3))
#=======================================================
# collections
from collections import deque
data = deque([2,3,4])
data.appendleft(1)
data.append(5)
print(data)
print(list(data))
# Counter
from collections import Counter
counter = Counter(['red','blue','red','green','blue','blue'])
print(counter['blue'])
print(counter['green'])
print(dict(counter))
#=========================================================
# math
import math
# factorial
print(math.factorial(5))
# 제곱근
print(math.sqrt(7))
# 최대공약수
print(math.gcd(21,14))
# pi, e
print(math.pi)
print(math.e)
#==========================================================