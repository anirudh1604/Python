class Node  :
    def __init__(self,data) :
        self.data=data
        self.next=None

class LinkedList :
    def __init__(self,data) :
        self.head=Node(data)
    def insertAtLast(self,data) :
        current=self.head
        while(current.next is not None) :
            current=current.next
        current.next=Node(data)
    def insertAtBegin(self,data) :
        node=Node(data)
        node.next=self.head
        self.head=node
    def listLength (self) :
        count =0
        current=self.head
        while (current is not None) :
            current=current.next
            count+=1
        return count
    def printList(self) :
        current=self.head
        while(current is not None) :
            print(current.data)
            current=current.next 
    def search (self,data) :
        current=self.head
        flag=0
        while (current is not None) :
            if (current.data == data) :
                flag=1
                break
            current=current.next
        if (flag==1) :
            print ("Found it !")
        else :
            print ("Not Found")
    def removeDuplicate(self) :
        current=self.head
        previous=Node(None)
        s=set()
        while(current is not None) :
            if (current.data in s) :
                previous.next=current.next
            else :
                s.add(current.data)
                previous=current
            current=current.next


ll=LinkedList(5)
ll.insertAtBegin(7)
ll.insertAtBegin(8)
ll.insertAtBegin(9)
print(ll.listLength())
print("\n")
ll.printList()
print("\n")
ll.insertAtLast(2)
ll.insertAtLast(3)
ll.insertAtLast(4)
print(ll.listLength())
print("\n")
ll.printList()
for i in range(0,15) :
    ll.search(i)


ll.insertAtBegin(9)
ll.insertAtBegin(9)

ll.insertAtBegin(9)

ll.insertAtBegin(9)

ll.insertAtBegin(9)

ll.insertAtBegin(7)

ll.insertAtBegin(7)

ll.printList()
print(ll.listLength())

ll.removeDuplicate()
print(ll.listLength())
