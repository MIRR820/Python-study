# 2557번 문제
print('Hello World!')

# 10718번 문제
print('강한친구 대한육군')
print('강한친구 대한육군')

# 1000번 문제
a, b = map(int, input().split())

print(a+b)

# 1001번 문제
a, b = map(int, input().split())

print(a-b)

# 10998번 문제
a, b = map(int, input().split())

print (a*b)

#1008번 문제
a, b = map(int, input().split())

print (a/b)

#10869번 문제
a, b = map(int, input().split())

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)

# 10926번 문제
a = input()

print(a+'??!')

# 18108번 문제
a = int(input())

print(a-543)

# 3003번 문제
data = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]
result = []

for i in range(6):
    value = chess[i] - data[i]
    result.append(value)
for n in range(6):
    print(result[n], end=" ")

# 10430번 문제
a, b, c = map(int, input().split())

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)

# 2588번 문제
a = int(input())
b = input()
c = list(b)

print(a*int(c[2]))
print(a*int(c[1]))
print(a*int(c[0]))
print(a*int(b))