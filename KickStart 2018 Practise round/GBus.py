fw = open("A-large.in","r")
fo=open("output.txt","w")
testcase=int(fw.readline())
for i in range(1,testcase+1):
    string=""
    buses=int(fw.readline())
    input=fw.readline()
    input=input.split()
    list = []
    for z in range(buses):
        start=int(input[0])
        end=int(input[1])
        for y in range(start,end+1):
            list.append(y)
        input.pop(0)
        input.pop(0)
    readlines=int(fw.readline())
    for k in range(readlines):
        point=int(fw.readline())
        counter=list.count(point)
        print(counter)
        string=string+str(counter)+" "
    fo.write("Case #"+str(i)+": "+string+"\n")


    fw.readline()
fw.close()
fo.close()