# **공부한 내용**

##### -내장함수 map 

여러 자료형을 받아 각각의 함수가 입력으로 들어간 다음 나오는 출력값을 리스트로 돌려줌 

Ex )

 `A,B = map(int.input().split())` # A, B 입력

 `print(A+B)` # A+B 출력

#### -자료형

숫자, 문자 등의 자료형태

| 자료형             | Ex            |
| ------------------ | ------------- |
| 정수 ( int )       | 1, 100, 12    |
| 실수( float )      | 3.14 , 314e-2 |
| 복소수 ( complex ) | 3+4j          |
| 불 (bool)          | True, False   |
| 문자 ( str )       | 'Hi'          |

```
i= 100
type(i) # type함수를 통해 자료형을 알 수 있음
```



|                  | 순서 | 중복 | 변경 |
| :--------------: | :--: | :--: | :--: |
|  리스트( list )  |  O   |  O   |  O   |
|  튜플 ( tuple )  |  O   |  O   |  X   |
|    셋 ( set )    |  X   |  X   |  O   |
| 딕셔너리 ( dict) |  X   |  X   |  O   |

##### print  함수  개 그리기

```
|\_/|
|q p|   /}
( 0 )"""\
|"^"`    |
||_/=\\__|
```

```
print("|\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\__|")   #"는 \"\로 표현하여 나타낸다.
```

#### 각 자리수 분리

**1. 문자열로 변환 후, 분리하는 방법**

변수 numer = 123에 대하여, list 변수에 넣기

```
a = []
for i in str(number):
    a.append(i)
```

str 후 int로 변환

**2. 10으로 나누어 자릿수 분리하기**

```
a = []
while(number!=0):
    a.append(number%10)
    x = x//10
```

원소는 int 값

**3. map 함수를 활용하여 원소값 더하기**
```
sum(map(int, str(number))
```

#### sys 모듈

sys 모듈은 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈.

EX)

```
#input 대신 sys.stdin.readline 출력 속도 증가
import sys

T = int(sys.stdin.readline())

for i in range(0,T) :
    A,B = map(int,sys.stdin.readline().split())
    print(A+B)
```

