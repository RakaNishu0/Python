class Cal(object):
    _history = []                       # 생성자(Constructor) 앞에 정의하는 클래스 변수.

    def __init__(self, v1, v2):         # __init__ = initialize (초기화, =Constructor) 인스턴스를 생성할 때마다 수행되는 것을 정의한다.
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2

    def add(self):
        result = self.v1+self.v2
        Cal._history.append("add : %d+%d=%d" % (self.v1, self.v2, result))      # 문자열 속에 변수를 가져오기
        return result

    def subtract(self):
        result = self.v1-self.v2
        Cal._history.append("subtract : %d-%d=%d" % (self.v1, self.v2, result))
        return result

    def setv1(self, v):                 # setv1 메소드를 생성하여, 직접 인스턴스 변수를 변경하지 않도록 함
        if isinstance(v, int):          # 만약 setv1 메소드의 입력값이 정수라면 True
            self.v1 = v                 # 정수일 때에만 self.v1 인스턴스변수에 그 입력값(v)을 대입시켜 줌 (v1 = v)

    def getv1(self):
        return self.v1

    @classmethod                        # 클래스 메소드 생성
    def history(cls):                   # 클래스 메소드는 인자로 cls = 클래스의 인자를 그대로 받는다
        for item in Cal._history:       # 클래스 변수인 _history 를 가져와 사용 (반복작업)
            print(item)

    def info(self):
        return "Cal => v1 : %d, v2 : %d" % (self.v1, self.v2)


class CalMultiply(Cal):                 # Cal 클래스를 상속받아서 CalMultiply 라는 클래스를 생성한다
    def multiply(self):
        result = self.v1*self.v2
        Cal._history.append("multiply : %d*%d=%d" % (self.v1, self.v2, result))
        return result

    def info(self):
        return "CalMultiply => %s" % super().info()         # 부모 super()의 info()메소드를 사용할 것


class CalDivide(CalMultiply):           # CalMultiply 클래스를 상속받아서 CalDivide 라는 클래스를 생성한다
    def divide(self):                   # 상속의 상속,은 위의 상속자가 상속받은 내용을 모두 내려받을 수 있다.
        result = self.v1/self.v2
        Cal._history.append("divide : %d/%d=%d" % (self.v1, self.v2, result))
        return result

    def info(self):
        return "CalDivide => %s" % super().info()


c0 = Cal(30, 60)
print(c0.info())

c1 = CalMultiply(10, 10)
print(c1.info())

c2 = CalDivide(20, 10)
print(c2.info())
