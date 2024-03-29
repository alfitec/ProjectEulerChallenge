import functools
import time

#@functools.cache    7_270_635_184 ns
# no cache          90_860_122_448 ns

@functools.cache 
def CollatzLength(n):

    if (n==1): return 1

    if n%2==0: return CollatzLength(n/2)+1
    else:      return CollatzLength(3*n+1)+1

print(CollatzLength(13))

if __name__=='__main__':
    starttime=time.perf_counter_ns()
    longestCollatz=1
    numberForLngestSequence=1
    for i in range(1,1000001):
        tempRes=CollatzLength(i)
        if tempRes>longestCollatz:
            longestCollatz=tempRes
            numberForLngestSequence=i
    endtime=time.perf_counter_ns()
    print(f"{longestCollatz=}     {numberForLngestSequence=}   time={endtime-starttime}")
