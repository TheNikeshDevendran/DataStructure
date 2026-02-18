'''
Rotate the array from right hand side by k step where k is not negative
'''

# Method 1 #
arr=[1,2,3,5,6] 
k=3
# output shopuld be [5,3,1,2,3]
for i in range(k):
    arr.insert(0,arr.pop())
    print(f'step:{i}',arr)
print(arr)

# Method 2 #
num=[1,2,3,4,5,6,7]
k=5
# output [4,5,6,7,1,2,3]
if k<=len(num):
   num=num[-k:]+num[:-k]
   print(num)
else:
    print('K value is out of range ')
    print(num)

