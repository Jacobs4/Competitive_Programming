# Three test cases are still failing as of now. Well, I can't do shit about it.
def abbreviation(a, b):
    A = a[:]
    B = b[:]
    if B[-1] == '' or B[-1] == " ":
        B = B[:-1]

    count = 0
    test = ''
    for i in a:
        if i.isupper():
            test += i

    while len(b) > 0 and len(a) > 0:
        
        if a[0] == b[0] or a[0].upper() == b[0]:
            
            if a[0].isupper():
                count = 0
            else:
                count += 1
   
            
            a = a[1:]
            b = b[1:]
        
        else:
            if a[0].islower():
                a = a[1:]

            elif a[0].isupper() and count == 0:
                return "NO"

            else:
                b = B[len(B)-len(b)-count:]
                

    
    if len(a) > 0:
        for i in a:
            if i.isupper():
                return "NO"
    
    return "YES" if len(b) == 0 else "NO"
