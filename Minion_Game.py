s=input()
vowels=['A','E','I','O','U']
k=0
p=0
for i in range(len(s)):
    if s[i] in vowels:
        k+=len(s)-i
    else:
        p+=len(s)-i
if k>p:
    print("k",k)
elif p>k:
    print("p",p)
else:
    print("draw")