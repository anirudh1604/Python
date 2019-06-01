graph={
    "a" : ["c"],

    "b" : ["c","e"],

    "c" : ["a","b","d","e"],

    "d" : ["c"],

    "e" : ["c","b"],

    "f" : []
}
def generate_edges(graph) :
    edges=[]
    for node in graph.keys() : ######get Keys(Vertices)
        for neighbour in graph[node] : ## Get Values(Edges)
            edges.append((node,neighbour))
    print(edges)

def find_isoted_node(graph) :
    isolated=[]
    for node in graph :
        if not graph[node] :
            #isolated+=node
            isolated.append(node)

    print(isolated)

#####generate_edges(graph)
#####find_isoted_node(graph)