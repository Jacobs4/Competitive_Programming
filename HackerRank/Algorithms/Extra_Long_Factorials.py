# Python gang got this one of easy.
def extraLongFactorials(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    print(ans)
