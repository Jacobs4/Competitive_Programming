# I know, This logic is dog shit, but hey it works, I just don't wanna think
def countApplesAndOranges(s, t, a, b, apples, oranges):
    s = s - a
    t = t - a
    count = 0
    for i in range(0, len(apples)):
        if apples[i] >= s and apples[i] <=t:
            count += 1
    print(count)
    count = 0
    s = s + a
    t = t + a
    a = b
    s = s - a
    t = t - a
    for i in range(0, len(oranges)):
        if oranges[i] >= s and oranges[i] <=t:
            count += 1
    print(count)        
    return
