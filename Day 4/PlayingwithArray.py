n = int(input())
lst = [int(i) for i in input().split()][:n]
ans = list()
sum = 0
for i in lst:
    sum  = sum + i
    print(sum,end=" ")
    
    