graph=[]
nodes=[]
node_count=0
def add_node(v):
    global node_count
    if v in nodes:
        print(v,"is already present in nodes")
    else:
        nodes.append(v)
        node_count+=1
        for row in graph:
            row.append(0)
        temp=[]
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)
"""
graph=[[0,0,0],
            [0,0,0],
            [0,0,0]]
nodes=["A","B","C"]
"""

def add_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"is not present in graph")
    elif v2 not in nodes:
        print(v2,"is not present in graph")
    else:
        ind1=nodes.index(v1)
        ind2=nodes.index(v2)
        graph[ind1][ind2]=1
        graph[ind2][ind1]=1
def printgraph():
    print(nodes)
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end=" ")
        print()
add_node("A")
add_node("B")
add_node("C")
add_edge("A","B")
printgraph()
