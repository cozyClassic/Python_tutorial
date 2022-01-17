"""
class parent :
    parent_name = "parent_name"
    
    def __init__(self, name) :
        self.name = name

    def print_names(self) :
        print("self.name : ", self.name)
        print("parent_name : ", self.parent_name) #self.parent_name 대신, parent.parent_name을 넣어도 동작한다.

#parent_instance = parent("parent_instance")

#parent_instance.print_self()
#print(parent_instance)


# 자식클래스의 선언. parent 클래스를 상속한다.
class child(parent):
    child_name = "child_name"

print(child.parent_name)
# parent_name
child.parent_name =  "chagned child"

print(child.parent_name)
# chagned!

print(parent.parent_name)
# parent_name 
# 자식요소의 변경이 부모 요소에게는 영향이 없는 것을 알 수 있음.

parent.parent_name = "changed parent"
print(child.parent_name)


# 인스턴스간의 관계
class Person :
    name    = "person name"
    age     = 18

    def __init__(self,name) :
        self.name = name

print(Person.name, Person.age)
# person name, 18

# 인스턴스 선언
p_instant1 = Person("인스턴트1")

#p_instant1.age = 20

print(p_instant1.name, p_instant1.age)
# 인스턴스 1, 20

Person.age = 33
print(p_instant1.name, p_instant1.age)


#print(Person.name, Person.age)
# person name, 18


#다중상속

class A:
    def greeting(self):
        print('안녕하세요. A입니다.')
 
class B(A):
    def hello(self) :
        print(1)

 
class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')
 
class D(B, C):
    pass
 
x = D()
x.greeting()

"""

#맹글링

class Mangling:
    def __init__(self) :
        self.name = "이름"
        self.hobby = "취미"

man = Mangling()
print(man.name, man.hobby)
#이름 취미

class Mangling2:
    def __init__(self) :
        self.name = "이름"
        self.__hobby = "취미"

man2 = Mangling2()
#print(man2.name, man2.hobby)
# Error : Mangling2 객체에는 'hobby' attribute가 없다.
#print(man2.name, man2.__hobby)
# # Error : Mangling2 객체에는 '__hobby' attribute가 없다...고 한다.

# print(dir(man2))
"""
['_Mangling2__hobby', '__class__', '__delattr__', '__dict__', '__dir__',
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
'__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
'__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name']
"""
print(man2._Mangling2__hobby)
# 취미 출력됨.

# 파이썬에서 맹글링을 적용한 속성은, _클래스명__속성명의 형태로 이름이 바뀌는 것 뿐이고, 외부에서의 접근을 막지는 못한다.

