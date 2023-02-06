graph={}
nodes=[]
def add_node(v):
    if v in nodes:
        print(v,"is already present in graph")
    else:
        nodes.append(v)
        graph[v]=[]
def add_edge(v1,v2):
    if v1 not  in nodes:
        print(v1,"is not present in graph")
    elif v2 not in nodes:
        print(v2,"is not present in graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)
def delete_node(v1):
    if v1 not in nodes:
        print(v1,"is not in graph")
        return
    nodes.remove(v1)
    graph.pop(v1)
    for i in graph:
        if v1 in graph[i]:
            graph[i].remove(v1)
def printgraph():
    print(nodes)
    for i in graph.items():
        print(*i)
add_node("A")
add_node("B")
add_node("C")
add_edge("A","C")
add_edge("A","B")

print("\nBefore deleting")
printgraph()

delete_node("C")

print("\nAfter deleting")
printgraph()
