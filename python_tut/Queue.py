class Queue :
    DEFAULT_CAPACITY=10
    def __init__(self) :
        self._data=[None]*Queue.DEFAULT_CAPACITY
        self._size=0
        self._front=0

    def _length(self) :
        return self._size

    def isEmpty(self) :
        return self._size == 0

    def first(self) :
        if self.isEmpty() :
            raise ('Stack is Empty') 
        return self._data[self._front]

    def dequeue(self) :
        if self.isEmpty() :
            raise ('Stack is Empty')
        answer=self._data[self._front]
        self._data[self._front]=None
        self._front=(self._front+1) % len(self._data)
        self._size -=1
        return answer
    def resize(self,New_Capacity) :
        old=self._data
        self._data=[None]*New_Capacity
        walk=self._front
        for k in range(self._size) :
            self._data[k]=old[walk]
            walk=(walk+1) % len(old)

        self._front=0
    
    def enqueue(self,data) :
        if  self._size==len(self._data) :
            self.resize(2*len(self._data))
        avail=(self._front + self._size)% len(self._data)
        self._data[avail]=data
        self._size += 1

queue = Queue()


for i in range(100) :
    queue.enqueue("Anirudh"+str(i))

print("After First")
print(queue._length())
print(queue.first())


for i in range(50) :
    print(queue.dequeue())



print(queue._length())
print(queue.first())


