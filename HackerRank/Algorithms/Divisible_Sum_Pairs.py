def divisibleSumPairs(n, k, ar):
    ans = 0
    ar.sort()
    for i in range(len(ar)):
        for j in range(i+1, len(ar)):
            if (ar[i]+ar[j])%k==0:
                ans+=1
    return ans
