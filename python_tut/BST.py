class Node :
    def __init__(self,data,pos) :
        self.left=None
        self.data=data
        self.right=None
        self.pos=pos
class Tree :
    def __init__(self,data) :
        self.root=Node(data,1)
        print(1)
    def insert (self,node,data,pos) :
        if node is None :
            print (pos)
            return Node(data,pos)
        if (data < node.data) :
            node.left=self.insert(node.left,data,2*pos)
        else :
            node.right=self.insert(node.right,data,(2*pos+1))
        return node

    def minNode(self,node) :
        current=node
        while current.left is not None :
            current=current.left
        return current
    
    def deleteNode(self,node,data,pos,printl,node_Parent) :
        if node is None :
            return node
        ###Searching a Node to be deleted
        if data < node.data :
            node.left=self.deleteNode(node.left,data,(2*pos),printl,node)
        elif data > node.data :
            node.right=self.deleteNode(node.right,data,(2*pos+1),printl,node)
        else : 
            if printl==1 :
                print(node.pos)
            
'''
try :
    flag=0
    for _ in range(int(input())) :
        inp=input().split()
        if (inp[0]=='i') :
            if (flag!=0) :
                tree.insert(tree.root,int(inp[1]),1)
                continue 
            tree=Tree(int(inp[1]))
            flag=1
        else :
            tree.root=tree.deleteNode(tree.root,int(inp[1]),1,1)
except :
    pass


tree=Tree(1)
tree.insert(tree.root,5,1)
tree.insert(tree.root,7,1)
tree.insert(tree.root,4,1)
tree.insert(tree.root,1,1)
tree.deleteNode(tree.root,1,1)
tree.deleteNode(tree.root,5,1)
tree.deleteNode(tree.root,8,1)
'''




tree=Tree(1)
tree.insert(tree.root,2,1)
tree.insert(tree.root,0,1)
tree.root=tree.deleteNode(tree.root,2,1,1,None)
tree.insert(tree.root,3,1)
tree.insert(tree.root,11,1)
print("Hello")
tree.root=tree.deleteNode(tree.root,1,1,1,None)
tree.insert(tree.root,8,1)
print("Hello")
tree.insert(tree.root,12,1)
tree.root=tree.deleteNode(tree.root,11,1,1,None)
tree.insert(tree.root,13,1)

