# # class Node:
# #     def __init__(self,data) -> None:
# #         self.pref = None
# #         self.data = data
# #         self.nref = None
# # class Doubly_Linked_List:
# #     def __init__(self) -> None:
# #         self.head = None
# #     def add_node(self,data):
# #         new_node = Node(data)
# #         if self.head == None:
# #             self.head = new_node
# #         else:
# #             temp = self.head
# #             while temp.nref:
# #                 temp = temp.nref
# #             temp.nref = new_node
# #             new_node.pref = temp
# #     def display(self):
# #         if self.head == None:
# #             print('Doubly_LinkedList is Empty')
# #         else:
# #             temp = self.head
# #             while temp.nref:
# #                 # print(temp.data,temp.nref)
# #                 if temp.pref == None:
# #                     print(None,'||',temp.data,'||',temp.nref.data,'|---->|',end='  ')
# #                 else:
# #                     print(temp.pref.data,'||',temp.data,'||',temp.nref.data,'|---->|',end='  ')
# #                 temp = temp.nref
# #             print(temp.pref.data,'||',temp.data,'||',None)
# # data = [10,20,30,40,50,60]
# # obj = Doubly_Linked_List()
# # for i in data:
# #     obj.add_node(i)
# # obj.display()

# # arr = [1,2,3,4,5]
# # arr1 = []
# # arr2 = []
# # slow = 0
# # fast = 1
# # for i in range(len(arr)):
# #     if fast == len(arr)-1:
# #         print(arr[slow],arr[-1],fast)
# #         arr1 = arr[:slow+1]
# #         arr2 = arr[slow+1:]
# #         break
# #     if fast == len(arr):
# #         arr1 = arr[:slow]
# #         arr2 = arr[slow:]
# #     fast += 2
# #     slow += 1
# # print(arr1,arr2)

# # while arr1 and arr2:
# #     print(arr1[0],arr2[-1], end=' ')
# #     arr1.pop(0)
# #     arr2.pop()



# nodes = []
# graph = []
# node_map = {}
# node_cnt = 0
# def add_node(n):
#     global node_cnt
#     if n in nodes:
#         print(f"{n} is already present in the graph")
#     else:
#         node_cnt += 1
#         nodes.append(n)
#         node_map[n] = []
#         for col in graph:
#             col.append(0)
#         row = []
#         for ele in range(node_cnt):
#             row.append(0)
#         graph.append(row)
# def add_edge(n1,n2):
#     if n1 not in nodes:
#         print(n1,'is not present in graph')
#     elif n2 not in nodes:
#         print(n2,'is not present in graph')
#     else:
#         ind1 = nodes.index(n1)
#         ind2 = nodes.index(n2)
#         graph[ind1][ind2] = 1
#         graph[ind2][ind1] = 1
#         node_map[n1].append(n2)
#         node_map[n2].append(n1)
# def print_graph():
#     print('Nodes:\n  ',nodes)
#     print('Node with edges:\n  ',node_map)
#     print('Graph:')
#     for row in graph:
#         print('  ',row)
# def bfs(root):
#     queue = [root]
#     res = [root]
#     while queue:
#         node = queue.pop(0)
#         node_adj = node_map[node]
#         for i in node_adj:
#             if i not in res:
#                 res.append(i)
#                 queue.append(i)
#     print(res)
# add_node('A')
# add_node('B')
# add_node('C')
# add_node('D')
# add_edge('A','B')
# add_edge('A','C')
# add_edge('A','D')
# add_edge('B','D')
# add_edge('C','D')
# bfs('B')
# print_graph()

# graph = []
# def add_graph():
#     for i in range(3):
#         temp = []
#         for j in range(3):
#             temp.append(0)
#         graph.append(temp)
# add_graph()

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class LL:
#     def __init__(self):
#         self.head = None
# n1 = Node(1)
# head = n1
# n2 = Node(2)
# n3 = Node(3)
# n1.next = n2
# n2.next = n3
# n3.next = n1
# temp = n1
# while temp:
#     print(temp.data)
#     temp = temp.next
#     if temp == head:
#         break

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
res = 0
temp = 0

start = 0
end = 0
curr_index = 0
for i in arr:
    temp+=i
    if temp > res:#start will be 0 untill the max sum is positive from beginning
        res = temp
        start = curr_index
        end = i
    if temp < 0:#start will be next element of the current element
        temp = 0
        start += 1
print(res,arr[start:end+1])
    