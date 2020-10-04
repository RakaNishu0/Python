def a3():
    return 'aaaaa'


print(a3())


def aa():
    print('before')
    return 'aa'         # return 은 결과값을 받는다. + return 이후의 문단은 무의미하다. 결과값은 return 의 뒤에 오는 값으로 지정되기 때문이다. = 결과값을 받았다면 함수는 완료된 것이다.
    print('after')     # = 결과값이 나왔기 때문에.


print(aa())


# return 으로 반환된 결과를 여러 곳에 여러 용도로 활용할 수 있다.


# print('a'*5)
# print('aaaaa')
