n,m=list(map(int,input().split()))
lst1 = [int(i) for i in input().split()][:n]
lst2 = [int(i) for i in input().split()][:m]
s = set()
for i in range(n):
    s.add(lst1[i])
for j in range(m):
    s.add(lst2[j])
print(len(s))