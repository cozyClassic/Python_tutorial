#iterators
strings = "ABC"

iters = iter(strings)

print(next(iters)) # A 
print(next(iters)) # B
print(next(iters)) # C
print(next(iters)) # Exception : StopIteration

def 함수():
    print("출력A")
    print("출력B")
   
함수() # 출력A, 출력B 출력됨.



def 함수2():
    print("출력A")
    print("출력B")
    yield

함수2() # 아무것도  출력되지 않음.
제너레이터 = 함수2()
print(제너레이터) # generator라는 객체가 됨. <generator object 함수2 at 0x7fadd009d820>
print(type(제너레이터)) # <class 'generator'>

#제너레이터 실행 방법 : next 사용하기.
next(제너레이터)

def 함수3():
    print("출력A")
    print("출력B")
    yield 100

제너레이터3 = 함수3()
값 = next(제너레이터3)
print(값) # 100이 출력됨.

#yield 의 뜻 : 내가 내 아래로 진행 안하고 양보할게!

def 함수4() :
    print("출력A")
    yield 100 # 1번째 멈춤
    print("출력B")
    yield 200
    print("출력C")
    yield 300
    print("출력D")
    yield 400

제너레이터4 = 함수4()
a = next(제너레이터4) # 출력A 실행
b = next(제너레이터4) # 출력B 실행
c = next(제너레이터4) # 출력C 실행
d = next(제너레이터4) # 출력D 실행

print(a,b,c,d) # 100, 200, 300, 400

#yield가 모두 끝난 이후에는, 더이상 실행되지 않음.
#즉, 1회용 함수라는 뜻이다.

numbers = [1,2,3,4,5]
이터레이터 = reversed(numbers)

for i in 이터레이터 : 
    print(i)
for i in 이터레이터 : 
    print(i)
# 한번만 사용된다.
# 이터레이터를 사용하면 메모리가 절약된다.
# 왜냐하면, 이터레이터 = reversed(numbers)를 선언할 때,
# numbers 전체를 갖고오는 것이 아니고, yield 실행 시마다, numbers에서 데이터를 하나씩 꺼내서 사용하는 개념이기 때문이다.
