from collections import Counter
def printElements(arr, n, k):
    val = 0
    x = n//k
    mp = Counter(arr)
    for it in mp:
        if mp[it] == x:
            val +=1
    print(val)
n,k=list(map(int,input().split()))
lst = [int(i) for i in input().split()][:n]

printElements(lst, n, k)