'''
Checking wether the linked list has a cyclic connection
[1,4,5,6]__
   ^       |
   |_______| 

If a linked list last node again points back to value in a list then
its a cyclic linked list
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
            NewNode.next=self.head
            cur.next=NewNode

    def Display(self):
        if self.head==None:
            print('Linked List is Empty')
        else:
            cur=self.head
            while cur:
                print(cur.data)
                cur=cur.next
    
    
ll=LinkedList()
ll.AddElement(10)
ll.AddElement(20)
ll.AddElement(30)
ll.AddElement(40)
ll.Display()
