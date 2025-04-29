from heapq import *
def MIN_HEAP():
    min_heap=[]
    for i in range(0,k,1):
	heappush(min_heap, arr[i])
    for i in range(k,n,1):
    	if(arr[i]>min_heap[0]):
            heappop(min_heap)
            heappush(min_heap,arr[i])
    print(min_heap)