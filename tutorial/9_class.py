"""
# 클래스 : 설계도 !!!
class car :
    # 내부데이터 
    # attribute = state (varaiable/value의 관계)
    model_name  = "name"
    model_year  = "year"
    model_color = "color"
    max_speed   = "speed"
    accel_sound = "sound"

    # 내부 함수 (method)
    def accelerate (self):
        sound = self.accel_sound
        print(sound)
    
    def name(self) :
        return self.model_name

# 클래스의 활용 :클래스로 할 수 있는것은 2가지(혹은 3가지)이다.

#1.인스턴스화 (선언) - 생성자 (constructor) 선언하지 않아서 그냥 basic 생성자가 사용됨.
mycar = car()

# 2. attribute 호출하기 : 호출하려면 dot(.) 을 사용한다.
print(mycar.model_name)
# attribute의 state를 변경할 수 도 있다.
mycar.model_name = "HI"
print(mycar.model_name)
# 3(2). 메소드 호출하기 : 그런데 메소드도 attribute의 일종 아닌가?
mycar.accelerate()

# 클래스를 갖고 뭔가 더 하는 것들은, 이 여러가지를 조합하는 것 뿐이다.

# 클래스의 구분
# mycar는 car 클래스의 인스턴스이다.
# mycar는 객체이다.

# 클래스의 데이터타입 : class 'type'
print(type(car)) 

# 인스턴스의 데이터타입 : class '__main__.car'
print(type(mycar))


# class person(): 과 class person : 의 차이
# class person() : 상속을 할거라고 해놓고 아무것도 안넣음.
# class person : 상속을 안함.
# class OO (__내용__) 의 __내용__ 에는, class가 상속할 다른 class 가 와야 한다.

# car 클래스를 상속받은 newcar클래스 선언
# 경고! 인스턴스 (mycar)를 상속하려고 했더니 제대로 작동하지 않았음.
class newcar(car) :
    def __init__(self,model_name) :
        self.name = model_name
    
    def show_name(self) :
        print("New car의 이름은 : ", self.name)

bentz = newcar("벤츠")
# newcar에는 없는 부모함수의 메서드, attr을 사용 가능.
bentz.accelerate()
print(bentz.model_name)

#참고 : 새로 생성한 인스턴스를 변경한다고 해서, 그게 부모 class에 영향을 미치지 않음.
print(car.model_name)

"""


# 스코프
# 파이썬의 특징은 global 문이 없을때, 변수에 선언하면 항상 내부의 스코프로 간다는 것이다.
# Local -> nonlocal -> Global
class scope_test():
    spam = "attribute spam"
    def do_local(self):
        spam = "local spam" # do_local 함수 내부 스코프의 spam에 할
    # def do_nonlocal(self):
    #     nonlocal spam
    #     spam = "nonlocal spam" # 바로 바깥에 있는 spam을 재연
    # def do_global(self):
    #      global spam
    #      spam = "global spam" # 완전 global의 spam에 재연결

test = scope_test()   
spam = "test spam"
#test.do_local()
#print("After local assignment:", spam)
#test.do_nonlocal()
#print("After nonlocal assignment:", spam)

#test.do_global()
print("After local assignment:", spam)

scope_test()
print("In global scope:", spam)

# After local assignment: test spam
# After local assignment: nonlocal spam
# After local assignment: nonlocal spam
# After local assignment: global spam

# 부모요소가 변하는지 거

print(scope_test().spam)

scope_test.spam = "changed"
print(scope_test().spam)