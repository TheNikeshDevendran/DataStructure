"""
Swapping in 5 diff ways
1.packing and unpacking method
2. Using Temp variable
3. Addition and Subtraction
4. Multiplication and Division
5. Using ^ xor operation
"""

# 1.packing and unpacking method
a=5
b=10
print('Before Swapping a and b:',a,b)
a,b=b,a
print('After Swapping a and b:',a,b)

# 2. Using Temp variable
c=7
d=8
temp=c
print('Before Swapping c and d:',c,d)
c,d=d,temp
print('After Swapping c and d:',c,d)

# 3. Addition and Subtraction
e=10
f=11
print('Before Swapping e and f:',e,f)
e=e+f # e=10,f=11 : 21
f=e-f # e=21,f=11 : 10
e=e-f # e=21,f=10 :11

print('after Swapping e and f:',e,f)

# 4. Multiplication and Division
g=6
h=5

print('Before Swapping g and h:',g,h)
g=g*h # g=6,h=5:30
h=g//h # g=30,h=5:6
g=g//h # g=30,h=6:5

print('After Swapping g and h:',g,h)

# 5. Using ^ xor operation
i=3
j=2
print('Before Swapping i and j:',i,j)
i=i^j #i=3:0011 , j=2:0010 =0001
j=i^j #i=0001 , j=2:0010 =0011
i=i^j #i=0001 , j=0011 = 0010
print('After Swapping i and j:',i,j)

