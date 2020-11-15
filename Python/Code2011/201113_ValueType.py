#=======================================================
# 리스트 컴프리헨션
# 0~19까지의 수 중에서 홀수만 포함하는 리스트 생성
array = [i for i in range(20) if i % 2 == 1]
print(array)
# 컴프리헨션을 사용하지 않는 경우
array2 = []
for i in range(20):
    if i % 2 == 1 :
        array2.append(i)
print(array2)
# 1부터 9까지 수의 제곱 값을 포함하는 리스트 생성
array = [i*i for i in range(1,10)]
print(array)
# n*m 크기의 2차원 배열을 0으로 초기화
n=3
m=4
array = [[0] * m for _ in range(n)]
print(array)
# remove_set에 포함되지 않는 숫자들만 포함하는 리스트
array = [1,2,3,4,5,6,7,8,9]
remove_set = {3,5}
result = [i for i in array if i not in remove_set]
print(result)
#=========================================================
# 문자열 자료형
data = "Hello World"
print(data)
data = "Don't you know \"Python\"?"
print(data)
# 문자열 연산
a = "Hello"
b = "World"
print(a + " " + b)
c = "String"
print(c*3)
d = "ABCDEFG"
print(d[2:4])
#===========================================================
# 튜플 자료형
# 튜플은 한번 선언된 값을 변경할 수 없다
# 튜플은 ()를 사용한다
a = (1,2,3,4)
print(a)
# a[2] = 7 -> error
#==========================================================
# 딕셔너리 자료형
# 딕셔너리는 키와 값을 쌍으로 갖는 자료형이다.
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'
print(data)
if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")
# 딕셔너리 자료형 관련 함수
key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)
for key in key_list:
    print(data[key])
#=========================================================
# 집합 자료형
# 집합은 둥복을 허용하지 않는다.
# 집합은 순서가 없다.
data = set([1,1,2,3,4,4,5])
print(data)
data = {1,1,1,2,3,4,4,5}
print(data)
# 집합 자료형 연산
a = {1,2,3,4,5}
b = {3,4,5,6,7}
print(a | b) # 합집합
print(a & b) # 교집합
print(a - b) # 차집합
# 집합 자료형 관련 함수
data = set([1,2,3])
print(data)
# 새로운 원소 추가
data.add(4)
print(data)
# 새로운 원소 여러 개 추가
data.update(([5,6]))
print(data)
# 특접 값을 갖는 원소 삭제
data.remove(3)
print(data)