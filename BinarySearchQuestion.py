'''
Create a function which will search the target lement in a array 
and return its index if present else return -1
'''

num=[20,30,40,50,60,90,100]
def BinarySearch(arr,target):
    low=0
    high=len(arr)-1
    flag=0
    while(low<=high):
        mid=low + (high-low)//2
        if target==arr[mid]:
           flag=1
           break
        elif target>arr[mid]:
           low=mid+1
        else:
            high=mid-1
    
    if flag==1:
        print(f'The value {target} is present in {mid} index')
    else:
        print(f'The value {target} is not present \nindex{-1}')

# BinarySearch(num,600)




''' Question: Take a sorted arary and find the start and end position of 
a target value
ex:[5,7,7,10,11]
target=7
Start_end_positon[1,2]
''' 
arr=[5,6,7,7,7,8,10]
target=0
start_end_position=[-1,-1]
low=0
high=len(arr)-1
while(low<=high):
    mid=(high+low)//2
    if target==arr[mid]:
        start_end_position[0]=mid
        high=mid-1

    elif target>arr[mid]:
        low=mid+1
    else:
        high=mid-1

# -----------------------------------

low=0
high=len(arr)-1
while(low<=high):
    mid=(high+low)//2
    if target==arr[mid]:
        start_end_position[1]=mid
        low=mid+1

    elif target>arr[mid]:
        low=mid+1
    else:
        high=mid-1

print(start_end_position)