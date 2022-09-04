import functools
import time

#@functools.cache    7_270_635_184 ns
# no cache          90_860_122_448 ns

@functools.cache 
def CollatzLength(n):

    if (n==1): return 0

    if n%2==0: return CollatzLength(n/2)+1
    else:      return CollatzLength(3*n+1)+1



if __name__=='__main__':
    starttime=time.perf_counter_ns()
    longestCollatz=1
    for i in range(1,1000001):
        tempRes=CollatzLength(i)
        if tempRes>longestCollatz:
            longestCollatz=tempRes
    endtime=time.perf_counter_ns()
    print(f"{longestCollatz=}     time={endtime-starttime}")
