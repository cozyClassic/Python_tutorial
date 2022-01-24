T = int(input())

def factorial(n) :
    result = 1
    for i in range(2,n+1) :
        result *= i
    return result

def solve(N,M) :
    return int(factorial(M) / (factorial(N) * factorial(M-N)))

for i in range(T) :
    N, M = map(int,input().split())
    print(solve(N,M))


"""
n C r =
n! / (r!) * (n-r)!

"""