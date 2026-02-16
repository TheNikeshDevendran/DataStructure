'''
BinarySearch is a searching technique to find a element in a 
sorted array or list by dividing the search space into half

Binary Search works on Sorted List only

time complexity
1.Beast case O(1)
2.Average case O(logn)
3.Worst case O(logn)
'''
arr=[10,60,90,50,20,30,55]
target=300 

low=0
high=len(arr)-1
flag=0

while(low<=high):
    mid=low+(high-low)//2
    if target==arr[mid]:
        flag=1
        break
    elif target>arr[mid]:
        low=mid+1
    else:
        high=mid-1
    


if flag==1:
    print('element found')
else:
    print('element not found')