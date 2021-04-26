A = set(input().split())
print(all([A.issuperset(set(input().split())) for _ in range(int(input()))]))