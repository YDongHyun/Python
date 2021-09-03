N = int(input())
P=N
a=[]
while True:
    if N>=10:
        M= (N%10) +(N//10)
    else : 
        M =N+0
    N=((N%10)*10)+(M%10)
    a.append(1)
    if P==N:
      break
print(len(a))


            
