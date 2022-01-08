def func(N) :
    sq = N * N
    while (N > 0) :
        if (N % 10 != sq % 10) :
            return False
        N //= 10
        sq //= 10
  
    return True
n = int(input())
if(func(n)):
    print("Phoenix number")
else:
    print("Not a phoenix number.")