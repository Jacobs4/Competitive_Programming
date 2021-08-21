# replace your function with this
def compareTriplets(a, b):
    ans = [0, 0]
    for i in range(0, 3):
        if a[i]>b[i]:
            ans[0] += 1
        if a[i]<b[i]:
            ans[1] += 1
    return ans
