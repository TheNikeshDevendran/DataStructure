'''
Check wether the give strign is an anagram
example:
cinema-iceman
study:dusty
'''
s='anagram'
t='nagaram'

# method1
s1=list(s)
t1=list(t)
s1.sort()
t1.sort()

if s1==t1:
    print('Its a anagram')
else:
    print('Its not a anagram')


# method2 :using hashmap technique
d1={}
d2={}
for char in s:
    if char in d1:
        d1[char]+=1
    else:
        d1[char]=1

for char in t:
    if char in d2:
        d2[char]+=1
    else:
        d2[char]=1

if d1==d2:
    print('its a anagram')
else:
    print('its not a anagram')

