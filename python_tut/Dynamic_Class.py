import ctypes
class Dynamic_Class :
    """A dynamic class for Python List"""
    def __init__(self):
        """Create an empty array"""
        self._n =0
        self._capacity=1
        self._A=self.__make_array(self._capacity)
    
    def __len__(self) :
        """Return no. of elements stored in the array """
        return self._n

    def __getitem__(self,k) :
        """Return element at index K """
        if not 0 <= k < self._n :
            raise IndexError('invalid index')
        return self._A[k]
    
    def __append__(self,obj) :
        """Add Object to end of the array """
        if self._n == self._capacity :
            self.__resize(2*self._capacity)
        self._A[self._n]=obj
        self._n+=1

    def __resize(self,c) :
        """Resize internal array to capacity c"""
        B=self.__make_array(c)
        for k in range (self._n) :
            B[k]=self._A[k]
        self._A=B
        self._capacity=c

    def __make_array(self,c):
        """Return new array with capacity c"""
        return (c*ctypes.py_object)()
    

obj=Dynamic_Class()
print(obj.__len__())

