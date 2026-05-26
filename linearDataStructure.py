'''
---------------------------------------
LIST/ARRAY
---------------------------------------
 OPERATION |   Where    | SPEED       |
---------------------------------------
 Accees    | anyposition| O(1)
---------------------------------------
insert     | end        | O(1)
---------------------------------------
insert     | middle     | O(n)
---------------------------------------
delete     | end        | O(1)
---------------------------------------
delete     | middle     | O(n)
---------------------------------------
slicing    | any range  | O(k) : k=[1:4]
'''

billNo=[30,40,50,10,60]

#accesing the element O(1)
print(billNo[-1])

# inserting the element at end O(1)
billNo.append(100)
print(billNo)

# inserting the element at a particular index O(n)
# [30, 40, 50, 200, 10, 60, 100]
#  0   1   2   3    4    5   6
billNo[3]=200 

# removing the element at last index O(1)
billNo.pop()

# removing the random element O(n)
billNo.pop(50)


