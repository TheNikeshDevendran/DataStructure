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

BinarySearch(num,600)