import asyncio
import time

# await를 사용한 함수
# 함수 앞에 async를 붙이지 않으면, await 를 사용하는것이 불가능하다.
async def prac1() :
    print('hello')          # hello 출력
    await asyncio.sleep(1)  # 1초 대기
    print('world!')         # world!

asyncio.run(prac1())



async def say_after(delay, what) :
    await asyncio.sleep(delay) # delay 만큼 기다린다.
    print(what)                # 입력값을 print 한다.

async def prac2() :
    print(f"시작시간 : {time.strftime('%X')}")

    await say_after(1, 'hello') # 1초 대기 후 'hello' 출력
    await say_after(2, 'world') # hello 출력 후 2초대기 후 'world' 출력

    print(f"종료시간 : {time.strftime('%X')}")

asyncio.run(prac2())


"""결과값
시작시간 : 15:56:56
hello
world
종료시간 : 15:56:59
"""


# 코루틴을 사용해서 두개의 함수를 동시에 실행시키기.
async def prac3() :
    print(f"시작시간 : {time.strftime('%X')}")
    
    await asyncio.create_task(say_after(1,'hello')) # 1초 대기 후 'hello' 출력
    await asyncio.create_task(say_after(2,'world')) # hello의 출력을 기다리지 않고, 2초 대기 후 'world' 출력
    # create_task : 코루틴 실행함수

    print(f"종료시간 : {time.strftime('%X')}")


# awaitable

async def nested() :
    return 42

async def awaitable_prac1() :
    # 단순히 nested()를 하는 것으로는 아무일도 일어나지 안흔다.
    # 코루틴 객체가 생성되지만, 대기하지는 않는다.
    # 따라서 nested() 함수는 '전혀 실행되지 않는다.'
    nested() # 에러가 발생하진 않지만, 경고(RuntimeWaring)가 발생한다.

    print(await nested())

asyncio.run(awaitable_prac1())

print("정상작동!")


async def awaitable_prac2() :
    # nested() 함수가 동시실행 되도록 예약한다.
    # main()과 함께
    task = asyncio.create_task(nested())

    # "task"는 이제 nested()를 취소할 때 사용된다.
    # 혹은 동작이 완료될 때까지 그냥 대기할 수도 있다.
    await task

asyncio.run(awaitable_prac2())