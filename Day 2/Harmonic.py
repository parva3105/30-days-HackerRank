def harmon(n):
    if(n<2):
        return 1
    else:
        return float((harmon(n - 1))+ 1/n)
n = int(input())
value = harmon(n)
ans = format(value,".4f")
print("Harmonic sum upto 4 decimal places:",ans)