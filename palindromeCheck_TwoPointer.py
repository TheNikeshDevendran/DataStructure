'''
We have to check wether the string is palindrome or not
requirements:string can be alpha-numerical no special character

note:' ' empty string is also a palindrome 
'''

s='A man, a plan, a canal: Panamacc'
# s='-mmomm  '
left=0
right=len(s)-1
flag=''
while(left<right):
    while (left<right and not s[left].isalnum()):
        left+=1
    while (left<right and not s[right].isalnum()):
        right-=1
    if (s[left].lower()!=s[right].lower()):
        flag=False
        break
    left+=1
    right-=1
    flag=True


if flag:
    print('Its a Palindrome')
else:
    print('Not a Palindrome')

