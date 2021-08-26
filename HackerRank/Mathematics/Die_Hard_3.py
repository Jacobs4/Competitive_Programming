def solve(a, b, c):
    if c<=max(a, b) and c%math.gcd(a,b)==0:
        return "YES"
    return "NO"
