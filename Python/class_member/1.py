# 인스턴스의 내부값을 가질 필요가 없는 메소드는 클래스 멤버로 만들어준다
# 인스턴스 멤버 =/= 클래스 멤버


# 파이썬은 static method 와 class method 의 두가지 종류가 있다

class Cs:
    @staticmethod
    def static_method():
        print("static method")

    @classmethod
    def class_method(cls):
        print("class method")

    def instance_method(self):
        print("instance method")


i = Cs()
Cs.static_method()
Cs.class_method()
i.instance_method()