class Cal(object):
    def __init__(self, v1, v2):         # __init__ = initialize (초기화) 인스턴스를 생성할 때마다 수행되는 것을 정의한다.
        if isinstance(v1, int):         # if, v1이 int의 인스턴스가 맞다면 True or False (여기서는 정수가 맞는지를 판단)
            self.v1 = v1                # self.v1 = instance 변수로서의 v1 을 정의한다.
        if isinstance(v2, int):
            self.v2 = v2                # self.을 붙이지 않은 v1은 __init__ 함수의 로컬변수일 뿐이므로 add()등에서 불러올 수 없다.

    def add(self):                      # add() 에도 self를 추가하여 instance 변수를 가져올 수 있도록 함
        return self.v1+self.v2

    def subtract(self):
        return self.v1-self.v2

    def setv1(self, v):                 # setv1 메소드를 생성하여, 직접 인스턴스 변수를 변경하지 않도록 함
        if isinstance(v, int):          # 만약 setv1 메소드의 입력값이 정수라면 True
            self.v1 = v                 # 정수일 때에만 self.v1 인스턴스변수에 그 입력값(v)을 대입시켜 줌 (v1 = v)

    def getv1(self):
        return self.v1


c1 = Cal(10, 10)
# print(c1.add())
# print(c1.subtract())

c1.setv1(20)                            # setv1() 메소드를 이용해서 값을 조정하는 방법 (권장)
c1.v2 = 30                              # c1.v2 인스턴스 변수에 직접 값을 입력하여 조정하는 방법
print(c1.add())
print(c1.subtract())
