from heapq import *
def MAX_HEAP():
    max_heap=[]
    for i in range(n):
	arr[i]=-arr[i]
    for i in range(0,k,1):
	heappush(max_heap,arr[i])
    for i in range(k,n,1):
        if(-arr[i]<-(max_heap[0])):
	    heappop(max_heap)
	    heappush(max_heap,arr[i])
    for i in range(0,k,1):
	max_heap[i]=-max_heap[i]
    print(max_heap)