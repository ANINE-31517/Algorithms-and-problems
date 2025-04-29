#Counting Sort
#Time : O(len(arr))
#Space : O(len(arr)+K)
#where K is the extra space taken by the dict(d)
for _ in range(int(input())):
    arr=list(map(int,input().split()))
    d={}
    for i in range(1,max(arr)+1):
        d[i]=0
    for i in arr:
        if i in d:
            d[i]+=1
    for i,j in d.items():
        i=str(i)
        if j!=0:
            print((i+" ")*j,end="")