
# class GrandMother :

#     family = "grandparents"

#     def print_self(self) :
#         print(self)
    
#     def print_HI():
#         print("HI!")

# LEE = GrandMother()

# GrandMother.print_HI()
# # 출력 내용 : HI!

# LEE.print_self()
# # 출력 내용 : <__main__.GrandMother object at 0x7ff4b814bf10>

# print(LEE)
# # 출력 내용 : <__main__.GrandMother object at 0x7ff4b814bf10>


# class father(GrandMother) :
#     FAMILY = "parents"

#     def __init__(self,name,age) :
#         self.name = name
#         self.age  = age
#         self.home = "seoul"

# KIM = father("Yong",40)
# # 정상 작동

# print(KIM.home)
# # seoul
# print(KIM.FAMILY)
# # parents
# """
# class Person :
#     name    = "person name"
#     age     = 18

#     def __init__(self,name) :
#         self.name = name

# p_instant1 = Person("인스턴트1")

# print(Person.name, Person.age)
# # person name 18

# Person.age = 33

# print(Person.name, Person.age)
# # person name 33  -- 클래스의  age가 변경됬음.

# print(p_instant1.name, p_instant1.age)
# # 인스턴트1 18 -- name은 변경되지 않고, age만 변경됬음.


# class Student :
#     name = "학생"

# Park = Student()

# Park.name 

# Park.name = "박개똥"

# Park.name
# """

# class School :
#     def __init__(self) :
#         self.name = "청담중학교"
#         self.loc  = "서울"
#         self.__born = "1990년 1월 15일"
    
#     def __hello(self) :
#         print("hello")

# school = School()
# #print(school.name, school.loc, school.__born)
# #AttributeError: 'School' object has no attribute '__born'

# print(dir(School))
# print(dir(school))

# class Test :
#     def __hello(self) :
#         print("hello")

# test2 = Test()

# #test2.__hello()
# #AttributeError: 'Test' object has no attribute '__hello'

# print(dir(Test))
# print(dir(test2))

class HI :
    def hello():
        print("hello")
    
    @staticmethod
    def statichello() :
        print("hello")

HI.hello()
#hello

HI.statichello()
#hello


hi = HI()
# 인스턴스 선언

#hi.hello()
#TypeError: hello() takes 0 positional arguments but 1 was given

# hi.statichello()
# #hello

# def trace(func):                             # 호출할 함수를 매개변수로 받음
#     def wrapper():                           # 호출할 함수를 감싸는 함수
#         print(func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
#         func()                               # 매개변수로 받은 함수를 호출
#         print(func.__name__, '함수 끝')
#     return wrapper                           # wrapper 함수 반환
 
# def hello():
#     print('hello')
 
 
# #trace_hello = trace(hello)    # 데코레이터에 호출할 함수를 넣음
# #trace_hello()                 # 반환된 함수를 호출
# trace(hello)()

# def trace(func):                             # 호출할 함수를 매개변수로 받음
#     def wrapper():
#         print(func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
#         func()                               # 매개변수로 받은 함수를 호출
#         print(func.__name__, '함수 끝')
#     return wrapper                           # wrapper 함수 반환
 
# @trace    # @데코레이터
# def hello():
#     print('hello')

from abc import ABCMeta, abstractmethod

class abstest(metaclass=ABCMeta) :
    @abstractmethod
    def should_make(self):
        self.name = "반드시 만들어져야 한다."

def decorator(func) :
    def wrapper() :
        print(func)
    
    return wrapper

@staticmethod
@classmethod
@abstractmethod
@decorator
def HelloWolrd() :
    print("HELOOO WORLD!!")