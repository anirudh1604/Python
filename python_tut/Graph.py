import Graph_Practice as gp
class Graph :
    def __init__ (self,graph_dict=None):
        if (graph_dict==None) :
            graph_dict={}
        self.__graph_dict=graph_dict
    def vertices(self) :
        return list (self.__graph_dict.keys)
    def edges(self) :
        return gp.generate_edges(self.__graph_dict)
    
