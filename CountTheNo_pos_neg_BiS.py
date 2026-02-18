'''
Trying to count thee no of positive and negative values 
using two pointer technique
'''
arn=[-3,-2,-1,1,2]
low=0
high=len(arn)-1
p=0
n=0
# trying to find the last negative index
neg_last_oc=-1
while(low<=high):
    mid=(low+high)//2
    if arn[mid]<0:
        low=mid+1
    else:
        high=mid-1

n=low
print('negative count',n)

low=0
high=len(arn)-1
while(low<=high):
    mid=(high+low)//2
    if arn[mid]<=0:
        low=mid+1
    else:
        high=mid-1

p=len(arn)-low
print('positive',p)