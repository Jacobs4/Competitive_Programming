def breakingRecords(scores):
    min = scores[0]
    max = scores[0]
    ans = [0, 0]
    for i in range(1, len(scores)):
        if scores[i] < min:
            min = scores[i]
            ans[1] += 1
        if scores[i] > max:
            max = scores[i]
            ans[0] += 1
    return ans
