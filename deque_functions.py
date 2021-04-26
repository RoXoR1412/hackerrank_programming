from collections import deque
d=deque()
for _ in range(int(input())):
    function,*value=input().split()
    getattr(d,function)(*value)
[print(x,end=' ')for x in d]