def sockMerchant(n, ar):
    ar.sort()
    ans = 0
    temp = -20
    for i in ar:
        if temp == i:
            ans += 1
            temp = -20
        else:
            temp = i
    return ans
