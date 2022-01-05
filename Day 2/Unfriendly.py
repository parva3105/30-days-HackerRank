n = int(input())
num = str(n)
check = True
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if(num[i]==num[j]):
            check = False
            break;
if(check):
    print("The number is lucky.")
else: 
    print("The number is unlucky.")