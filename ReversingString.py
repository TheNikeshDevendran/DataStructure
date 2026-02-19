'''
We have to check wether the string is palindrome or not
requirements:string can be alpha-numerical no special character

note:' ' empty string is also a palindrome 
'''
'''
a-z:97-122
A-Z:65-91
' ':32
'''
s='A man, a plan, a canal: Panama'
# defining the lower function logic
def Lower(s):
    S=''
    for char in s:
       if(char>='A' and char<='Z'):
          S+=chr(ord(char)+32)
       else:
          S+=char
    
    return S

# Defining isalnum logc to clean our string so that we can have only alphanumerical value
def IsAlNum(s):
    st=''
    for char in s:
       if (char>='A' and char<='Z') or (char>='a' and char<='z') or  (char>='0' and char<='9'):
          st+=char
    return st 
    
newS=Lower(s)
cleanedString=IsAlNum(newS)
print(newS)
print(cleanedString)

def CheckPalindrome(s):
    start=0
    end=len(s)-1
    while(start<=end):
        if(s[start]!=s[end]):
           return False
        start+=1
        end-=1
    return True

print(CheckPalindrome(cleanedString))