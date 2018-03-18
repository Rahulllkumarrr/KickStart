import time

t=time.time()
def f(K):
    N = 1
    while K > N:
        N *= 2
    
    if K == N:
        return 0
        
    return 1-f(N-K)

IN = open('B-large-practice.in', 'r')
OUT = open('output.txt', 'w')

NUM_TESTS = int(IN.readline())

for test in range(NUM_TESTS):
    K = int(IN.readline())
    answer = f(K)
    
    OUT.write('Case #{}: {}\n'.format(test+1, answer))
    print(str(test+1)+" "+str(answer))
print("Time : {}".format(time.time()-t))
IN.close()
OUT.close()
