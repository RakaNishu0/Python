# Variable

x = 10
print(x+5)


name = "RakaNishu"
print("Hello "+name+"!")                        # "+" 기호는 문자열 결합을 위한 문자연산자이다. 변수는 name으로 그냥 쓰임
# 다만, name 변수가 정의되지 않았다면 Error를 반환할 것
# 또한, 변수의 값이 문자가 아닌 숫자데이터라면 문자+숫자는 유효하지 않으므로 Error가 반환될 것이다

customer = "ywnee"                              # 중복되는 구문을 변수로 단일치환할 수 있다
print("Hello "+customer+"!")                    # 변경/수정에 있어서 중요한 부분이 된다 = 변수를 사용하는 이유
print(customer+" Welcome Home")

donation = 200                          # 변수의 이름 = 단순히 미지수가 아닌, 의미가 있어야 함
student = 10                            # 왜냐하면, 프로그래밍은 혼자 하는 것이 아닌, 유지보수성을 염두에 둬야하고,
sponsor = 30                            # 유지보수를 타인이 한다는 것을 가정하고, 타인도 알 수 있을 정도의 이름을 변수로 지정하는 것이 좋다
print((donation*student)/sponsor)       # x,y,z 등으로만 변수를 정의한다면, 제3자가 봤을 때, 어떤 변수가 어떤 값을 의미하는지 어떻게 알 수 있겠는가?
