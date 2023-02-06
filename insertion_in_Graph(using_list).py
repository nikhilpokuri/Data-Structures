graph={}
nodes=[]
def add_node(v):
    if v in nodes:
        print(v,"is already present in graph")
    else:
        nodes.append(v)
        graph[v]=[]
def printgraph():
  print(graph)
add_node("A")
add_node("B")
add_node("C")
printgraph()

