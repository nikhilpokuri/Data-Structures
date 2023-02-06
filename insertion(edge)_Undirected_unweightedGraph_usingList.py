graph={}
nodes=[]
def add_node(v):
    if v in nodes:
        print(v,"is already present in graph")
    else:
        nodes.append(v)
        graph[v]=[]
def add_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"is not present in graph")
    elif v2 not in nodes:
        print(v2,"is not present in graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)
def printgraph():
  for i in graph.items():
      print(*i)
#adding_nodes
add_node("A")
add_node("B")
add_node("C")
add_node("D")
#adding_edges
add_edge("A","B")
add_edge("A","D")
printgraph()
