def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)
n = int(input())
val = n
sum =0
while(n>0):
    digit = n%10
    if(digit >1):
        sum =sum + fact(digit)
    else:
        sum = sum+1
    n=int(n/10)
if(sum==val):
    print("Yes")
else:
    print("No")