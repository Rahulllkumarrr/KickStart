IN = open('D-small-attempt11.in', 'r')
OUT = open('output.txt', 'w')

NUM_TESTS = int(IN.readline())

for test in range(NUM_TESTS):
    N, Q = map(int, IN.readline().split())

    A = [int(i) for i in (IN.readline().split())]
    print(test, N)


    # returns (# of elements less than s, sum of those elements)
    def lessThan(s):
        return_count = 0
        return_sum = 0

        t = 0
        u = 0
        j = 0
        for i in range(N):
            while j < N and t + A[j] < s:
                t += A[j]
                u += A[j] * (j - i + 1)
                j += 1
                return_count += j - i
                return_sum += u

            if j > i:
                u -= t
                t -= A[i]
            else:
                j = i + 1

        return return_count, return_sum


    # returns sum of first n elements
    def sumOf(n):
        lower = 0
        upper = 100 * N + 1

        # binary search
        while lower + 1 < upper:
            mid = (lower + upper) // 2
            print(mid)
            m = lessThan(mid)[0]
            if m < n:
                lower = mid
            else:
                upper = mid

        a, b = lessThan(lower)
        return b + lower * (n - a)


    OUT.write('Case #{}:\n'.format(test + 1))
    for q in range(Q):
        l, r = map(int, IN.readline().split())
        OUT.write('{}\n'.format(sumOf(r) - sumOf(l - 1)))

IN.close()
OUT.close()
