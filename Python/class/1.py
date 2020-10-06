class Cal(object):
    def __init__(self, v1, v2):       # __init__ = initialize (초기화) 인스턴스를 생성할 때마다 수행되는 것을 정의한다.
                                    # (self) = 해당 instance 를 지칭한다.
        self.v1 = v1                # self.v1 = instance 변수로서의 v1 을 정의한다.
        self.v2 = v2                # self.을 붙이지 않은 v1은 __init__ 함수의 로컬변수일 뿐이므로 add()등에서 불러올 수 없다.

    def add(self):                  # add() 에도 self를 추가하여 instance 변수를 가져올 수 있도록 함
        return self.v1+self.v2

    def subtract(self):
        return self.v1-self.v2


c1 = Cal(10, 10)
print(c1.add())
print(c1.subtract())

c2 = Cal(30, 20)
print(c2.add())
print(c2.subtract())
