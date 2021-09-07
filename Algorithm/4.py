X = int(input())
k=0
while True:
  if X-k<=0:
    break
  else:
    X=X-k
    k+=1
c=[]
if k%2 ==1:
  for i in range(k):
    c.append("%d/%d"%(k-i,i+1))
else:
  for i in range(k):
    c.append("%d/%d"%(i+1,k-i))
  
print(c[X-1])
