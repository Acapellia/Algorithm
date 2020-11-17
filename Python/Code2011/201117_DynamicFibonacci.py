temp = [0] * 100
def calcFibonacci(n):
    if n==1 or n==2:
        return 1
    if temp[n] != 0:
        return temp[n]
    temp[n] = calcFibonacci(n - 1) + calcFibonacci(n - 2)
    return temp[n]
n = 99
print(f"Fibonacci {n} : {calcFibonacci(n)}")