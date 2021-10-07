# took a bit of damage for this one.
def appendAndDelete(s, t, k):
    c = 0
    l = len(s)
    while s[:l]!=t[:l]:
        l-=1
        c+=1
    o = ((len(t)-l)+c)
    if k<o:
        return "No"
    elif (len(s)+len(t))<=k:
        return "Yes"
    elif 2*len(t)<k:
        return "Yes"
    elif k%2 == o%2:
        return "Yes"
    else:
        return "No"
