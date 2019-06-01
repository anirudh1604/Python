class Stack :
    def __init__ (self) :
        self._data=[]
    def length (self) :
        return len(self._data)
    def isEmpty(self) :
        return len(self._data)==0
    def push(self,data) :
        self._data.append(data)
    def top(self) :
        if (self.isEmpty()) :
            raise ('Stack is underflow')
        return self._data[-1]
    def pop(self) :
        if (self.isEmpty()) :
            raise ('Stack is underflow')
        return self._data.pop()



stack=Stack()
stack.push("Anirudh")
stack.push("Prasoon")
print(stack.length())
print(stack.top())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.length())

