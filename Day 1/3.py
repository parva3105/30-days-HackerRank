def collatz_sequence(n):
    apped=list()
    while (n!=1) :
        apped.append(n) 
        if (n%2==0) :
            n=n/2
        else:
            n=(3*n)+1
    apped.append(1)  
    l=len(apped)
    print(l)
num  = int(input())
collatz_sequence(num)