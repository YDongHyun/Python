# 1~ 100 사이의 소수 출력
# 1과 자기자신만을 약수를 갖는 수


for i in range (2,101):
    for n in range(2,100):
        if n != i:
            if (i%n) != 0:
                print(i)
                break
            else:
                break
                
