n = int(input())
bin = list()
while(n!=0):
    bin.append(n%2)
    n= int(n/2)
for i in range(1,len(bin)+1):
    print(bin[-i],end= "")