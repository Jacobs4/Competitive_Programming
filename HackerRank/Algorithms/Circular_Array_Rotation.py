# wirite "from collections import deque" at the top where you inmport other libraries
from collections import deque
def circularArrayRotation(a, k, queries):
    temp = deque(a)
    temp.rotate(k)
    ans = []
    for i in queries:
        ans.append(temp[i])
    return ans
