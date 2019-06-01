class Comparator :

    def __init__(self,name,id) :
        self.Eid=id
        self.Ename=name

    def getEname(self) :
        return (self.Ename)
    def setEname(self,ename) :
        self.Ename=ename
    def getEid(self) :
        return (self.Eid)
    def setEid(self,id) :
        self.Eid=id

    

if __name__=='__main__' :
    lst=[]
    lst.append(Comparator("Anirudh",20))
    lst.append(Comparator("Prasoon",10))
    lst.append(Comparator("Prasoon4",4))
    lst.append(Comparator("Prasoon3",40))
    lst.append(Comparator("Prasoon1",6))
    lst.append(Comparator("Prasoon2",80))
'''for i in lst :
    print(i.getEid())    '''



lst=sorted(lst,key=(lambda x : x.getEname()),reverse=True)

for i in lst :
    print(i.getEid())    

