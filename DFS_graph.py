nodes = []
graph = []
node_map = {}
node_cnt = 0
def add_node(n):
    global node_cnt
    if n in nodes:
        print(f"{n} is already present in the graph")
    else:
        node_cnt += 1
        nodes.append(n)
        node_map[n] = []
        for col in graph:
            col.append(0)
        row = []
        for ele in range(node_cnt):
            row.append(0)
        graph.append(row)
def add_edge(n1,n2):
    if n1 not in nodes:
        print(n1,'is not present in graph')
    elif n2 not in nodes:
        print(n2,'is not present in graph')
    else:
        ind1 = nodes.index(n1)
        ind2 = nodes.index(n2)
        graph[ind1][ind2] = 1
        graph[ind2][ind1] = 1
        node_map[n1].append(n2)
        node_map[n2].append(n1)
res = []
visited = set()
def dfs(root):
    res.append(root)
    visited.add(root)
    for node in node_map[root]:
        if node not in visited:
            dfs(node)
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_edge('A','B')
add_edge('A','C')
add_edge('A','D')
add_edge('B','D')
add_edge('C','D')
dfs('A')
print(res)
