from math import floor

a, b = map(int, input().split())
for i in range(1, 1000000):
    if floor(i * 0.08) == a and floor(i * 0.1) == b:
        print(i)
        exit()
print(-1)
