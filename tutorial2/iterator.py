## 코딩도장의 이터레이터, 제너레이터, 코루틴, 데코레이터에 대해 정리

it = [1,2,3].__iter__()

print(it)
# 결과 : <list_iterator object at 0x7fb3e804f220>

print(it.__next__())
# 1
print(it.__next__())
# 2
print(it.__next__())
# 3

# print(it.__next__())
# 에러발생 : StopIteration 예외

it2 = "Hello World !".__iter__()

# print(len(it2))
# 에러발생 : iterator는 길이따위는 없다.

my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(3)
for i in my_set :
    print(i)


class Counter :
    def __init__(self, stop):
        self.current = 0 # 현재 숫자 유지, 0부터 지정된 숫자 직전까지 반복
        self.stop = stop # 반복을 끝낼 숫자

    def __iter__(self) :
        return self # 현재 인스턴스를 반환
    
    def __next__(self) :
        if self.current < self.stop : # 현재 숫자가 반복을 끝낼 숫자보다 작을 때
            r = self.current    # 반환할 숫자를 변수에 저장
            self.current += 1   # 현재 숫자를 1 증가시킴
            return r            # 숫자 반환
        else :
            raise StopIteration # 예외발생


for i in Counter(3) :
    print(i, end=' ')
# 결과 : 0,1,2

a,b,c = Counter(3)
print()
print(b)
# 1 


it = iter(range(3))

print(next(it))
print(next(it))
print(next(it))

# print(next(it))
# raiseError

it = iter(lambda : range(4), 2)
print(next(it))
print(next(it))


it = iter(range(3))
print(next(it,10)) # 0
print(next(it,10)) # 1
print(next(it,10)) # 2 
print(next(it,10)) # 10
print(next(it,10)) # 10