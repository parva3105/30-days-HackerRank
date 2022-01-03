n = int(input())
num = int(input())
prod= 1
sod = 0
while num>0:
    x = num%10
    sod = sod+x
    prod = prod*x
    num=int(num/10)
    
max_num= max(sod,prod)
min_num= min(sod , prod)

print(max_num-min_num)