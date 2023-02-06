graph={}
nodes=[]
def add_node(v):
    if v in nodes:
        print(v,"is already present in graph")
    else:
        nodes.append(v)
        graph[v]=[]
def add_edge(v1,v2,cost):
    if v1 not in nodes:
        print(v1,"is not present in graph")
    elif v2 not in nodes:
        print(v2,"is not present in graph")
    else:
        data1=[v1,cost]
        data2=[v2,cost]
        graph[v1].append(data2)
        graph[v2].append(data1)
def printgraph():
  for i in graph.items():
      print(*i)
#adding_nodes
add_node("A")
add_node("B")
add_node("C")
add_node("D")
#adding_edges(cost)
add_edge("A","B",3)
add_edge("A","D",4)
printgraph()
