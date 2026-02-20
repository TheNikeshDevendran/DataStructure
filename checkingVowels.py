s='IceCream'
d={'a':0,'e':0,'i':0,'o':0,'u':0,'A':0,'E':0,'I':0,'O':0,'U':0}
v=[]
for char in s:
    if char in d:
        d[char]+=1
        v.append(char)
print(d)
print(v)
ss=list(s)
left=0
right=len(ss)-1
while left<right:
    if ss[left] not in d:
        left+=1

    elif ss[right] not in d:
        right-=1
    else:
        ss[left],ss[right]=ss[right],ss[left]
        left+=1
        right-=1

print(ss)
        