n,m=input().split()
arr=input().split()
set1=set(input().split())
set2=set(input().split())
print(sum([(i in set1)-(i in set2) for i in arr]))