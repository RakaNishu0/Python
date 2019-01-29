# def a3():
#     return 'aaaaa'
#
# print(a3())
#
#
#
# def aa():
#     print('before')
#     return 'aa'         ## return은 결과값을 받는다. + return 이후의 문단은 무의미하다.
#     print('after')      ## = 결과값이 나왔기 때문에.
#
# print(aa())
#

## return 으로 반환된 결과를 여러 곳에 여러 용도로 활용할 수 있다.


# print('a'*5)
# print('aaaaa')


str = input('str 1 = ')
num = input('str 2 = ')

def make_string(str, num):
    return str+num

print(make_string(str, num))
