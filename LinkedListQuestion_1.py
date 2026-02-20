'''
Here we have  a linked list which contain a binary values 
so we need to get the decimal values out of it 
'''
class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None

    def AddElement(self,data):
        NewNode=Node(data)
        if self.head==None:
            self.head=NewNode
        else:
            cur=self.head
            while cur.next:
                cur=cur.next
            cur.next=NewNode
    
    def Display(self):
        if self.head==None:
            print('Linked List is Empty')
        else:
            cur=self.head
            while cur:
                print(cur.data)
                cur=cur.next

    def getDecimalValues(self):
        if self.head==None:
            print('Linked List is Empty')
        else:
            cur=self.head
            ans=0
            s=''
            while cur:
                ans=ans*2+cur.data
                s+=str(cur.data)
                cur=cur.next
            print(f'The decimal for of {s}:{ans}')


ll=LinkedList()
ll.AddElement(1)
ll.AddElement(0)
ll.AddElement(1)

ll.Display()
ll.getDecimalValues()
