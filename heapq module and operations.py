import heapq#MODULE OF MIN HEAP AND ITS OPERATIONS
lis=[100,30,255,10,34,8]

        #OPERATIONS
heapq.heapify(lis)#this method arranges the lis to min heap

heapq.heappushpop(lis,5)#this method pushes the given node and then removes smallest node

heapq.heapreplace(lis,1)#this method removes the smallest node and then replaces given node

nsmall=heapq.nsmallest(2,lis)#this method returns the 'n' number of  smallest nodes

nlarge=heapq.nlargest(3,lis)#this method returns the 'n' number of  largest nodes

print(nsmall)
print(nlarge)
print(lis)
