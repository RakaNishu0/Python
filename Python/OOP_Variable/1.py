class C(object):
    def __init__(self, v1):
        self.value = v1


c1 = C(10)
print(c1.value)         # ruby 와 다르게, Python 은 클래스의 외부에서 인스턴스 변수에 직접 접근이 가능하다.

print(c1)               # c1이 C() 라는 클래스에서 어떤 변수에 대입될 것인지가 정의되지 않아서 값이 아닌 메모리 주소를 보여줌

c1.value = 20           # 이렇게 외부에서도 직접 인스턴스 변수에 값을 입력하는 것이 가능함.
print(c1.value)
