data = list(map(int, input().split()))
modulo = int(input())
print(list(map(lambda x: x % modulo, data)))
