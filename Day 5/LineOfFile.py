n = int(input())
a = int(input())
b = int(input())
print(n - max(a + 1, n - b) + 1)