from copy import deepcopy

N,M=map(int,input().split())

c=[]
for i in range(N):
    A=str(input())
    b=list(A)
    c.append(b)

d=[]
s=[]
r=0
for i in range(N-7):
    for j in range(M-7):
        r=0
        d=deepcopy(c)
        
        
        for k in range(i,i+8):
            for p in range(j,j+8):
               
                if k==i:
                    if d[k][p]=='B':
                        if p<j+7 and d[k][p+1]!='W':
                            d[k][p+1]='W'
                            r+=1              
                        
                    else:

                        if p< j+7 and d[k][p+1]!='B':
                            d[k][p+1]='B'
                            r+=1
    
                else:
                    if d[k-1][p]==d[k][p]:
                        if d[k-1][p] == "B":
                            d[k][p]="W"
                            r+=1
                        else:
                            d[k][p]="B"
                            r+=1
        s.append(r)

for i in range(N-7):
    for j in range(M-7):
        r=0
        d=deepcopy(c)
        
        
        for k in range(i,i+8):
            for p in range(j,j+8):
                if p==j and k==i:
                    if d[k][p]!='W':
                        d[k][p]='W'
                        r+=1
                elif k==i:
                    if d[k][p]=='B':
                        if p<j+7 and d[k][p+1]!='W':
                            d[k][p+1]='W'
                            r+=1              
                        
                    else:

                        if p< j+7 and d[k][p+1]!='B':
                            d[k][p+1]='B'
                            r+=1
    
                elif k!=i:
                    if d[k-1][p]==d[k][p]:
                        if d[k-1][p] == "B":
                            d[k][p]="W"
                            r+=1
                        else:
                            d[k][p]="B"
                            r+=1
        s.append(r)
        

print(min(s))
