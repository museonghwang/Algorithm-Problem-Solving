n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

result = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')