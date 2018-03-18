import time
t=time.time()
def sub_lists(my_list):
    subs = []

    for i in range(len(my_list)):
        n = i + 1
        while n <= len(my_list):
            sub=my_list[i:n]
            sub = [int(i) for i in my_list[i:n]]
            total=sum(sub)
            subs.append(total)
            n=n+1
    return subs

fo= open("D-small-attempt11.in", "r")
fw = open("output.txt", "w")
testCases = int(fo.readline())
for testCase in range(1, testCases + 1):
    fw.write("Case #" + str(testCase) + ": \n")
    sp=fo.readline()
    sp=sp.split()
    numEle=int(sp[0])
    queries=int(sp[1])
    inputlist=fo.readline()
    numlist=inputlist.split()
    all=sub_lists(numlist)
    all.sort()
    for q in range(queries):
        line=fo.readline().split()
        l=int(line[0])-1
        r=int(line[1])
        series=all[l:r]
        #print(series)
        s_total=int(sum(series))
        fw.write(str(s_total)+"\n")
    print("Time : ",time.time()-t)
fo.close()
fw.close()