def fun(arr, n):
    found = False
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (arr[i] + arr[j] + arr[k] == 0):
                    found = True
    if (found == True):
        print("true")

n = int(input())
arr = [int(i) for i in input().split()][:n]
fun(arr,n)