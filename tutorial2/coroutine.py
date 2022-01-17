def number_coroutine() :
    while True : 
        x = (yield)
        print(x)

co = number_coroutine()

next(co)        # 코루틴 안의 yield까지 코드 실행 (최초실행)

co.send(1) # 코루틴에 숫자 1을 보냄
co.send(2) # 코루틴에 숫자 2을 보냄


def sum_coroutine() :
    total = 0
    while True : 
        x = (yield total) 
        # 코루틴 밖에서 값을 받아오면서 밖으로 값을 전달
        total += x

co = sum_coroutine()
#print(next(co)) # 0 : 코루틴 안의 yield까지 코드를 실행 + 코루틴의 반환값 출력
print(co.send(None)) # send(None)으로 next(co)를 대체할 수 있다.

print(co.send(1)) # 1 : 코루틴에 숫자 1을 보내고 반환값 출력
print(co.send(2)) # 3 : 코루틴에 숫자 2을 보내고 반환값 출력 
print(co.send(3)) # 6 : 코루틴에 숫자 3을 보내고 반환값 출력 


def onetime_coroutine() :
    total = 0
    x = (yield total)
    # next(co2) 단계에서는 x = (yield) 상태에서 일시정지
    # co.send(5) 에서 x = 5 를 할당받음
    total += x
    # total += x 로 total = 5 가 됨
    x = (yield total)
    # x = (yield)에서 다시 일시정지가 일어나면서, total = 5 를 반환함.

co2 = onetime_coroutine()
print(next(co2))
print(co2.send(5))
# print(co2.send(10)) 비정상 종료

def close_coroutine() :
    try :             
        while True :
            x = (yield)
            print(x, end=' ')
 
    except GeneratorExit:    # 코루틴이 종료 될 때 GeneratorExit 예외 발생
        print()
        print('코루틴 종료')
 

co = close_coroutine()
next(co)

for i in range(10) :
    co.send(i)

co.close()

# next(co) 
# StopIteration 예외발생


def accumulate() :
    total = 0 
    while True :
        x = (yield)         # 코루틴 밖에서 값을 받아온다.
        if x is None :      # 받은 값이 none 이면 total 반환
            return total
        total += x

def sum_coroutine() :
    while True :
        total = yield from accumulate()
        print(total)

co = sum_coroutine()
next(co)

for i in range(1,11) :
    co.send(i)
co.send(None)           # 끝내기

for i in range(11,21) :
    co.send(i)
co.send(None)