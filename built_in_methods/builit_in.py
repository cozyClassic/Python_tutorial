

#1. all(iterable)
# 전부 True인지 확인한다.
print("ALL - Boolean 값 반환")
print(all([1,2,3,4,5]))
# True
print(all([1,2,3,4,5,0])) # 0 => False
# False
print(all(["",1,2,3,4])) # "" => False
# False
print(all([]))
# True

#2. Any(iterable)
# 하나라도 True인지 확인한다.
print("Any - boolean값 반환")
print(any([]))
#False
print(any([1]))
#True
print(any([0]))
# False
print(any([0,1]))

#3. repr(object)
test = [1,2,3]
print(repr(test))
# [1,2,3]


#4. eval(expression) # expression은 문자열이어야 함.
x = [4,5,6]
print(eval('test')+eval('x'))
#[1,2,3,4,5,6]
test2 = 'print("HI!")'
eval(test2)
#HI!
print(eval(test2))
#None

#5. ascii(object) #  뭔지 잘 모르겠다.
print(ascii("A"))
print(ascii(")"))
print(ascii("ABCD+1234"))
ascii(test)


#6. callable(object) 
# call "()" 이 가능한 객체인지 아닌지를 판별한다.
print(callable(print))
#True
print(callable(print()))
#False

def call_func() :
    return "callable test"
call_var = "callable test"
print(callable(call_func))
#True
print(callable(call_var))
#False
print(callable(1+1))
#False


#7. chr(int)
# 유니코드 포인트가 i 인 문자열을 반환한다.
# ord() 와의 반대 기능을 한다.
print(chr(50), type(chr(50)))
# 2, <class 'str'>
print(chr(97), type(chr(97)))
# a, <class 'str'>


#8. @classmethod
