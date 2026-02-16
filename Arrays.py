arr=[10,50,30,20,40]
# append will add  element at end of an array
arr.append(60)

# pop will remove last index element by default if we do no provide the index 
# or if i provide index as 55 which is not actually there the we will get error
arr.pop()
arr.pop(100)

# remove will remove a particular value from the list 
# ex:remove(20) and if 20 occurs multiple time it will remove only the first occurence of it
arr.remove(20)

# index will provide index of particular value
arr.index(20)

print(arr)