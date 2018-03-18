fo=open("B-large-practice.in","r")
fw=open("out.txt","w")
arr=['']
def twicked(n):
    list1 = list(str(n))
    for x in range(len(list1)):
        if list1[x] == "1":
            list1[x] = "0"
        else:
            list1[x] = "1"
    rev=reversed(list1)
    list2 = "".join(rev)
    return list2
def string(n):
    last=len(arr)-1
    for i in range(n):
        if n <= 1:
            return 0
        else:
            temp=arr[0]+'0'+twicked(arr[0])
            arr.pop(0)
            arr.append(temp)
            print("{} is complete".format(i+1))
            print(len(arr[0]))
        #temp=temp+"0"+twicked(temp)
        #if i==n-1:
            #print(str(i+1)+" : "+str(temp))
    return arr[0]
def answer(k):
    n=1
    while k>n:
        n=n*2
    if k==n:
        return 0
    return 1-answer(n-k)
test=int(fo.readline())
n=60
for i in range(1,test+1):
    position=int(fo.readline())
    number=str(answer(position))
    fw.write("Case #"+ str(i) +": "+number+"\n")
fo.close()
fw.close()