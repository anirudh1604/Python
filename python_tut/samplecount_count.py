class sampleclass: 
    count = 0     # class attribute 
  
    def __init__(self,name) :
        self.name = name

    def increase(self): 
        sampleclass.count += 1
    @classmethod
    def fun(cls,name) : #needs 'self' as a parameter, since it is a class method and not a function.
        print ("Hello")
        return cls(name)
    @staticmethod
    def fun_S():
        print ("Hello_S")
  
# Calling increase() on an object 
s1 = sampleclass("anirudh") 
s1.increase()   
s1.fun()
s1.fun_S()      
print (s1.count) 
print (s1.name)
  
# Calling increase on one more 
# object 
s2 = sampleclass("prasoon") 
s2.increase() 
print (s2.count) 
  
print (sampleclass.count) 
