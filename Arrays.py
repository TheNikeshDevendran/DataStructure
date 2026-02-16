arr=[10,50,30,20,40]
# append will add  element at end of an array
arr.append(60)

# pop will remove last index element by default if we do no provide the index 
# or if i provide index as 55 which is not actually there the we will get error
arr.pop()
# arr.pop(100)

# remove will remove a particular value from the list 
# ex:remove(20) and if 20 occurs multiple time it will remove only the first occurence of it
arr.remove(20)

# index will provide index of particular value
# if i am trying to find a value index which is not in the list then i will raise error
arr.index(10)

# extend will merge two list
arr.extend([1,2])


# Traversing 
li=[20,30,40,50,60]
for index in range(0,len(li)):
    print(li[index])

for ele in li:
    print(ele)