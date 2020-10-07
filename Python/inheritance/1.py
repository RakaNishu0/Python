# inheritance

class class1(object):               # 오리지널 클래스가 있고, 여기에 새로운 메소드를 추가하여 활용하고 싶음
    def method1(self):
        return 'A1'


c1 = class1()
print(c1.method1())

print('=== 1st test ===')
# if not inheritance - 상속 없이 위 클래스에 새로운 메소드를 추가하고 싶을 때

class class2(object):               # class2가 상속을 활용하지 않으면
    def method1(self):              # class1과 동일한 방법으로 method1을 만들고
        return 'A1'

    def method2(self):              # 추가하고 싶은 메소드를 정의하게 된다.
        return 'A2'                 # 이 부분은 필연적으로 '중복'을 발생시킬 수밖에 없다.


c2 = class2()
print(c2.method1())
print(c2.method2())

print('=== 2nd test ===')
# using inheritance - 상속 개념을 활용하는 경우

class class3(class1):                   # 상속 개념을 활용하는 경우, 'object' 대신 상속할 class 이름을 가져오고,
    def method3(self):                  # 그 밑에는 추가할 메소드를 작성하기만 하면 된다. 중복도 없고 훨씬 깔끔한 문장을 만들 수 있다.
        return 'A3!!!'                  # 생성자(=__init__)도 필요 없다. 부모에서 생성자를 그대로 받아옴


c3 = class3()
print(c3.method1())                     # 상속을 하는 경우, class3 에서 method1 이 있는지 확인하고, 없으면 상속받은 class1에 method1이 있는지 찾아서 활용
print(c3.method3())                     # 결과값은 상속받은 것과 추가한 것이 잘 나타나고 있다.