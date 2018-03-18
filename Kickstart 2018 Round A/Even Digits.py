fr=open("large.txt","r")

fw=open("outputLarge.txt","w")

test=int(fr.readline().strip())


def valid(n):
    arr=[int(k) for k in str(n)]
    for z in arr:
        if z%2==1:
            return False
    return True


for i in range(1,test+1):
    print("case ",i)
    num=int(fr.readline().strip())
    neg=num
    pos=num
    times=0
    while True:
        if valid(neg)==False and valid(pos)==False:
            neg=neg-1
            pos=pos+1
            times+=1
        else:
            fw.write("Case #{}: {}\n".format(i,times))
            break

fr.close()
fw.close()


