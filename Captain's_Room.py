k=int(input())
s=list(int,input().split())
myset=set(s)
print(((sum(myset)*k)-sum(s))//(k-1))
