def pickingNumbers(a):
    temp = [0]*100
    ans = []
    for i in a:
        temp[i]+=1
    for i in range(len(temp)-1):
        ans.append(temp[i]+temp[i+1])
    return max(ans)
