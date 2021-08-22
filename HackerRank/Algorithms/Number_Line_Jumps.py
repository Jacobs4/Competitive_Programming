def kangaroo(x1, v1, x2, v2):
    if (x1>=x2 and v1>=v2) or (x1<=x2 and v1<=v2):
        return "NO"
    k = abs(x1-x2)/abs(v1-v2)
    k = int(k)
    if x1 + v1 * k == x2 + v2 * k:
        return "YES"
    else:
        return "NO"
