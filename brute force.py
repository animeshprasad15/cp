import sys
def ip(): return sys.stdin.readline()
def oP(s): sys.stdout.write(str(s)+'\n')
import operator as op
from functools import reduce
L=lambda:map(int,ip().split())
for _ in range(int(ip())):
    n=int(ip())
    l=list(L())
    s=0
    i=j=0
    while i<n:
        j=i+1 
        while j<(n+1):
            k=reduce(op.mul, l[i:j], 1)
            # oP(k)
            if k%4==0:
                s+=1
                s+=(n-j)
                j=n
            elif k&1==1:
                s+=1
            j+=1
        i+=1
    oP(s)
