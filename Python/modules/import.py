# def a():
#     return 'a'
# # 복잡한 코드 (의 생략)
# def a():
#     return 'BB'
# # 복잡한 코드 (의 생략)
# print(a())          ## 결과값은 BB가 나올 수밖에 없다.
#
#
# print("-------")
#


import mod1,mod2        ## 복수의 모듈을 불러온다

print(mod2.a())
print(mod1.a())


from mod1 import b as c     ## mod1 모듈안의 b 함수만 c라는 이름으로 불러옴

print(c())              ## c()는 b()를 직접 함수로 불러왔으므로 mod1. 이 필요없음
print(mod2.a())         ## a()는 mod2를 통째로 불러왔으므로 mod2.을 붙여 구분해줘야 함
