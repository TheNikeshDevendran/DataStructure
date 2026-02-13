num=int(input('enter the number:'))
temp=num
rev=0
while(num!=0):
    lastTerm=num%10
    rev=rev*10+lastTerm
    num=num//10

if temp==rev:
    print('its palindrome')
else:
    print('its not a palindrome')