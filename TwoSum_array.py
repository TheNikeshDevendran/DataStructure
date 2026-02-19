'''
Here we have given with a array and we need to find a pair which will 
become as target variable

ex:[2,3,4,5,1]
target=5
pairs:[2,3] [4,1]
but we need to give only one pair
and solve it by time complexity O(n)^2
'''
'''
in Dictionary what ever operation we are performing it will take only
O(1)
'''
# method 1...
arr=[2,1,5,6,3,3,4]
target=6
pairs=[]
for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print([arr[i]+arr[j],i,j])
            break

# method 2...

# using hashmap
def two_sum_all_pairs(arr, target):
    seen = {}         
    result = []       
    for i, num in enumerate(arr):
        needed = target - num
        if needed in seen:
            result.append((seen[needed], i))
        seen[num] = i
    return result

arr = [2,4,5,1,0,7]
target = 6

print(two_sum_all_pairs(arr, target))
