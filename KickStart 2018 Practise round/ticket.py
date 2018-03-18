fo=open("input.txt","r")
fw=open("output.txt","w")
#def count(n):

test=int(fo.readline())
for tests in range(1,test+1):
    tickets=int(fo.readline())
    arr1=[]
    arr2=[]
    for z in range(2*tickets):

    for i in range(tickets):
        start=fo.readline().strip()
        end=fo.readline().strip()
        arr2.append(start+"-"+end)
    print(arr2)
    '''d=0
    for y in range(tickets):
        arr2.append(list(arr1[d:d+2]))
        d=d+2
        print(arr2)'''
fo.close()
fw.close()