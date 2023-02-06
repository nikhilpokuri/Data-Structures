def add_node(v):
    global node_count
    if v in nodes:
        print(v,"is already present in Nodes")
    else:
        nodes.append(v)
        node_count+=1
        #if we add extra Node the graph must include extra ROW and COLUMN
        for row in graph:#to add 0 at the end of every ROW in graph
            row.append(0)
        temp=[]
        for i in range(node_count):#to add 0 at the end of every COLUMN in graph
            temp.append(0)
        graph.append(temp)
def printgraph():
    print(nodes)
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end=" ")
        print()
nodes=[]
graph=[]
node_count=0
add_node("A")
add_node("B")
add_node("C")
printgraph()
