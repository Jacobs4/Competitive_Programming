def birthday(s, d, m):
    ans = 0
    sum = 0
    j=0
    if len(s) == 1 and m == 1 and s[0] == d:
        return 1
    for i in range(m):
        sum += s[i]
    for i in range(m, len(s)):
        if sum == d:
           ans += 1
        sum = sum - s[j] + s[i]
        j += 1
    if sum==d:
        ans+=1
    return ans
