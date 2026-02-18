'''
We will try to reverse a arra of string using Bianry search
and should use the same array 
'''
    #  0   1   2   3   4   5
arr=['n','i','k','e','s','h']
print('Before Reverse:',arr)
low=0
high=len(arr)-1
while(low<high):
    arr[low],arr[high]=arr[high],arr[low]
    print([low,high])
    low+=1
    high-=1

print('After Reverse:',arr)