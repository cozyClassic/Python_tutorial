def number_generator() :
    yield 0
    yield 1
    yield 2

for i in number_generator() :
    print(i)

# 0,1,2 출력

g = number_generator()

a = next(g)
print(a)

b = next(g)
print(b)

c = next(g)
print(c)


def number_generator_for(stop) :
    n = 0                   # 숫자는 0부터 시작
    while n < stop :        # 현재 숫자가 반복을 끝낼 숫자보다 작을 때 반복
        yield n             # 현재 숫자를 밖으로 전달
        n  += 1             # 현재 숫자를 증가시킴

for i in number_generator_for(3) :
    print(i)
    # 0, 1, 2 출력


def number_generator_from() :
    x = [1,2,3]
    for i in x : 
        yield i

for i in number_generator_from():
    print(i)
    # 1,2,3 출력

def number_generator_from_2():
    x = [1,2,3]
    yield from x

for i in number_generator_from_2():
    print(i)
    # 1,2,3 출력

def number_generator_for_n(stop) :
    n = 8
    while n < stop :
        yield n
        n += 1

def ten_generator() :
    yield from number_generator_for_n(10)

for i in ten_generator() :
    print(i)
    # 8, 9 출력