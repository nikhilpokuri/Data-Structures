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
        row = [0 for _ in range(node_cnt)]
        # for ele in range(node_cnt):
        #     row.append(0)
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
def isbiparte(root):
    clr_arr = [-1]*node_cnt
    stack = [root]
    while stack:
        u = stack.pop(0)
        for v in node_map[u]:
            if graph[u][v] == 1 and graph[u][u] == 1:#self loop
                print('Given Graph is not Biparte')
                return
            if graph[u][v] == 1 and clr_arr[v] == -1:
                clr_arr[v] = 1 - clr_arr[u]
                stack.append(v)
            elif graph[u][v] == 1 and clr_arr[u] == clr_arr[v]:
                print('Given Graph is not Biparte')
                return
    print('Given Graph is Biparte')
    return

def print_graph():
    print('Nodes:\n  ',nodes)
    print('Node with edges:\n  ',node_map)
    print('Graph:')
    for row in graph:
        print('  ',row)
add_node(0)
add_node(1)
add_node(2)
add_node(3)
add_edge(0,1)
# add_edge(0,2)
add_edge(1,2)
add_edge(2,3)
print_graph()
isbiparte(0)
