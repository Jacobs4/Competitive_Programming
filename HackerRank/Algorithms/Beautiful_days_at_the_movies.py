def beautifulDays(i, j, k):
    ans = 0
    for i in range(i, j+1):
        temp = ""
        temp2 = i
        for j in range(0, len(str(i))):
            temp += str(temp2%10)
            temp2 = temp2//10
        if abs(i-int(temp))%k==0:
            ans+=1
    return ans
