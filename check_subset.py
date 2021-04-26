for _ in range(int(input())):
    _,set1=int(input()),set(map(int,input().split()))
    _,set2=input(),set(map(int,input().split()))
    print( set1.issubset(set2))