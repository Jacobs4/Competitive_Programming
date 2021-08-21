#people who are not using python, this ain't gonna work for them, you need to change the datatypes may to long long ?

#replace your function with this
def aVeryBigSum(ar):
    ans = 0
    for  i in range(0, len(ar)):
        ans += ar[i]
    return ans
