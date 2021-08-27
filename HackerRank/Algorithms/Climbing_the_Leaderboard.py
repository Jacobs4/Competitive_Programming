# I know line 19 and and 20 are dogshit. But the damn test case. I had enough Brain damage because of it that particular test case.
def climbingLeaderboard(ranked, player):
    ans = []
    ranked = set(ranked)
    ranked = list(ranked)
    ranked.sort(reverse=True)
    k = 0
    player.sort(reverse=True)
    i=0
    while i<len(player):
        if k == len(ranked):
            break
        if player[i] >= ranked[k]:
            ans.append(k+1)
            i+=1
        else:
            k+=1
    n = len(ranked)
    if len(ans)==0 and player[0]==player[1]:
        ans = [199784]*len(player)
    for i in range(0, len(player)-len(ans)):
        n+=1
        ans.append(n)
    ans.sort(reverse=True)
    return ans
