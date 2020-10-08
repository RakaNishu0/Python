# 클래스 변수

class Cs:
    count = 0                       # class 내부 + method 외부에 있는 변수는
    def __init__(self):             # class 변수로서 정의 되고
        Cs.count = Cs.count + 1     # 이 변수는 Cs.count 처럼 클래스내부 변수로 호출해서 사용

    @classmethod
    def getCount(cls):              # 클래스메소드는 반드시 첫 인자를 넣어주도록 되어 있다
        return Cs.count             # cls = Cs 클래스 자체를 인자로 받는다.

i1 = Cs()
i2 = Cs()
i3 = Cs()
i4 = Cs()

print(Cs.getCount())
