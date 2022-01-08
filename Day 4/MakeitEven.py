def count(lst):
    cnt = 0
    for i in lst:
        if(len(str(i))%2==0):
            cnt += 1
    print(cnt)
n = int(input())
lst = [int(i) for i in input().split()][:n]
count(lst)