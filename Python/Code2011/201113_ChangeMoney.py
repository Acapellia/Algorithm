# 이것이 코딩테스드다 with 파이썬 - 87p, 거스름돈
# 그리디 알고리즘
def ChangeMoney(money):
    moneyType = [500,100,50,10]
    cnt = 0
    for m in moneyType:
        cnt += int(money / m)
        money = money % m
    return cnt

if __name__ == '__main__':
    result = ChangeMoney(1260)
    print(result)