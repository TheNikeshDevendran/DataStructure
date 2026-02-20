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
    
    def GetMiddle(self):
        '''
        Here We are Using the tortise and the Rabbit race as a example
        slow(tortise)=it will move one step a head
        fast(rabbit)=it will move two step a head
        '''
        slow=self.head
        fast=self.head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        print('This is the middle element',slow.data)

ll=LinkedList()
ll.AddElement(10)
ll.AddElement(20)
ll.AddElement(30)
ll.AddElement(40)
ll.AddElement(50)
ll.AddElement(510)
ll.AddElement(500)
ll.AddElement(502)
ll.AddElement(509)
ll.Display()
ll.GetMiddle()
