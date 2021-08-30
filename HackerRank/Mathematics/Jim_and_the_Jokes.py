def dec(base, n):
    ans = 0
    for i in str(n):
        if int(i) >= base:
            return -1
        ans = (int(i)+ans*base)
    return ans


def solve(dates):
    change = [0]*100
    for i in range(len(dates)):
        base = int(dates[i][0])
        day = dates[i][1]
        tod = dec(int(base), day)
        if tod != -1:
            change[tod] += 1
    ans = 0
    change.sort(reverse=True)
    for i in change:
        ans += (i*(i-1)//2)
    return ans
