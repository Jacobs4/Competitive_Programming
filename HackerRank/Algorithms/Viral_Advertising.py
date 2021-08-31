def viralAdvertising(n):
    ans = 0
    people = 5
    for i in range(n):
        ans += people//2
        people = (people//2)*3
    return ans
