def a():
    return 'a'
# 복잡한 코드 (의 생략)
def a():
    return 'BB'
# 복잡한 코드 (의 생략)
print(a())          ## 결과값은 BB가 나올 수밖에 없다.


print("-------")


def name_a():               ## 함수 앞에 '작성자의 이름'을 써서 분류...
    return 'a'
# 복잡한 코드 (의 생략)
def name2_a():              ## 가능은 하지만 비효율적..
    return 'BB'

print(name_a())
