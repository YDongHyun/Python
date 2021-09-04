import sys

N = int(sys.stdin.readline())
for i in range(N):
    a = list(sys.stdin.readline())
    s = 0
    score=0
    b=[]
    for n in range(len(a)):
        if a[n]=='O':
            score=score+1
            s=s+score
            
        else :
            b.append(s)
            score=0
            s=0
    b.append(s)
    print(sum(b))
