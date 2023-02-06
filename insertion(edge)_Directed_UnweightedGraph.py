def add_node(v):
    global count_nodes#global is used to access and modify global variables
    if v in nodes:
        print(v,"is already present in graph")
    else:
        nodes.append(v)
        count_nodes+=1
        for i in graph:
            i.append(0)
        col=[]
        for j in range(count_nodes):
            col.append(0)
        graph.append(col)
def add_edge(v1,v2,cost):
    if v1 not in nodes:
        print(v1,"is not present in graph")
    elif v2 not in nodes:
        print(v2,"is not present in graph")
    else:
        ind1=nodes.index(v1)
        ind2=nodes.index(v2)
        graph[ind1][ind2]=1
def printgraph():
    print(nodes)
    for row in range(count_nodes):
        for col in range(count_nodes):
            print(graph[row][col],end=" ")
        print()
graph=[]
nodes=[]
count_nodes=0
add_node("A")
add_node("B")
add_node("C")
add_edge("A","B",3)
add_edge("A","C",4)
printgraph()
        
