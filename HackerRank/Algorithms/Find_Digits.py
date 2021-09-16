def findDigits(n):
    line = str(n)
    ans = 0
    for i in line:
        if int(i) != 0 and n%int(i) == 0:
            ans += 1
    return ans
