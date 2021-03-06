class C(object):
    def __init__(self, v1):
        # self.value = v1
        self.__value = v1               # 인스턴스변수 이름 앞에 __ 를 붙여주면, 외부에서는 접근할 수 없는 속성을 갖게 된다

    def show(self):
        print(self.__value)
    # def getValue(self):
    #     return self.value
    # def setValue(self, v1):
    #     self.value = v1


c1 = C(10)
# print(c1.__value)         # 접근할 수 없기 때문에 에러가 발생
c1.show()                   # 하지만 show() 메소드는 __value 에 접근할 수 있기 때문에 그 값만 출력해줄 수 있음

# print(c1.value)           # ruby 와 다르게, Python 은 클래스의 외부에서 인스턴스 변수에 직접 접근이 가능하다.
# print(c1.getValue())        # 그럼에도 별도의 메소드를 사용해 가져오는 방식
#
# # c1.value = 20             # 이렇게 외부에서도 직접 인스턴스 변수에 값을 입력하는 것이 가능함.
# c1.setValue(20)             # 그럼에도 별도의 메소를 사용해 입력하는 방식
# print(c1.value)

# 왜? 메소드를 통해 제어하는가?
