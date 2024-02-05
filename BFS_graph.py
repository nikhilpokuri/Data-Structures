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
def print_graph():
    print('Nodes:\n  ',nodes)
    print('Node with edges:\n  ',node_map)
    print('Graph:')
    for row in graph:
        print('  ',row)
def bfs(root):
    queue = [root]
    res = [root]
    visited = {root}
    while queue:
        node = queue.pop(0)
        node_adj = node_map[node]
        for i in node_adj:
            if i not in visited:
                res.append(i)
                queue.append(i)
                visited.add(i)
    print(res)

add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_edge('A','B')
add_edge('A','C')
add_edge('A','D')
add_edge('B','D')
add_edge('C','D')
bfs('B')
print_graph()