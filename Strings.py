# ASCII stands for American Standard Code for Information Interchange.
'''
strings are IMMUTABLE in nature
97-122 :a-z
65-91 :A-Z

'''

str1='NikeshNNN'
# give the total lene of string
print(len(str1))

# max will give the char which has highest unciode value from the string
print(max(str1))

# min is opposite to max
print(min(str1))

# it takes only one character and return unicode of it
print(ord(str1[0]))

# if we give unicod it wil return char of it
print(chr(ord(str1[0])))

# swapcase if somthing is in lower it wil convert to upper
# vice versa :lower<---->upper
print(str1.swapcase())

# count will check the no of occurance in the string
print(str1.count('i'))

# index will index of particular value 
# if value is present it will give index wlse error
print(str1.index('N'))


# it will replace the value with other character it all occurances
# if we wan to limit it we can provide the no of occurances
print(str1.replace('N','n',2))

# it will remove the left and right empty spaces
print(str1.strip()) 
# along with space if i want to remove a character using strip i  can achieve that
s='  ---------Nikesh@@@@@@@@@'
# here i want to remove space along with -,#
print(s.strip(' -@'))

# split will make a list of given string
s2='python is used in backend development'
print(s2.split())
# by default split take character after space
# if my string is : "apple,orange,grapes"
s2="apple,orange,grapes"
print(s2.split(','))

# it will check wether the string contain number or character
# and return output in true/false
print(str1.isalnum())

# it check wether the string contain only character
print(str1.isalpha())

# True if the string is a digit string, False otherwise.

print(str1.isdigit())


# defining length function
s1="Nikesh"
c=0
for i in s1:
    c+=1

print(f'The length of {s1}:',c)

#defining our count function
count_string='i'
c=0
for char in s1:
    if count_string==char:
        c+=1

print(f"The count of {count_string} is",c)   
