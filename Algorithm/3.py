a = ["c=","c-","dz=","d-","lj","nj","s=","z="]

c=list(input())
k=0
k2=0
for i in range(0,len(c)-1):
    if c[i] == "c" :
        if (c[i+1] == "=") or (c[i+1] == "-"):
            k+=1
    elif c[i] == "d":
        if c[i+1]=="-":
            k+=1
        elif c[i+1]== "z":
            if len(c)>i+2:
                if c[i+2] =="=":
                    k2+=1
    elif (c[i] == "l")and(c[i+1]=="j"):
        k+=1
    elif (c[i] == "n") and (c[i+1]=="j"):
        k+=1
    elif (c[i] == "s") and (c[i+1]=="="):
        k+=1
    elif (c[i] == "z") and (c[i+1]=="="):
        if i>0:
            if c[i-1]!="d":
                k+=1
        else:
            k+=1
    
print(len(c)-k-(2*k2))
