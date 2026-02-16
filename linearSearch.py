'''
Linear Search is a method of finding an item by checking
each element in the list one by one
''' 

arr=[20,50,90,400,5000,50,60,50]
searching_ele=50
flag=0
for ele in arr:
    if ele==searching_ele:
        flag=1
        break


if flag==1:
    print('Element Found')
else:
    print('Element Not Found')
 