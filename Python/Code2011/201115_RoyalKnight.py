data = input()
x = int(data[1])
y = int(ord(data[0])) - int(ord('a')) + 1
move = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1)]
result = 0
for m in move:
    tx = x + m[0]
    ty = y + m[1]
    if 1<= tx <= 8 and 1<= ty <= 8:
        result+=1
print(result)