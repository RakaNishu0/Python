inp_value = input("Your ID..? : ")              # python의 input()은 문자열로만 반환한다. 숫자를 입력하더라도 문자열이 된다.
print(type(inp_value))

real_raka = [11, "raka"]
real_nishu = "nishu"

#if inp_value == "raka":
#    inp_value = 11                              # input()의 값이 raka와 같다면 11로 변수의 값을 다시 지정한다
#elif inp_value == "11":
#    inp_value = 11
#else:
#    pass

if inp_value in real_raka:
    print("Hello raka with list")
#if real_raka == inp_value:                      # 문자열 vs 숫자의 비교이지만, 위에서 raka라고 입력한 것을 11로 변경했으므로 True가 된다
#    print("Hello raka")
elif real_nishu.upper() == inp_value.upper():
    print("Hello "+real_nishu)
#elif real_raka == int(inp_value):               # inp_value 변수를 int()로 감싸서, 문자열로 반환되는 input()의 값을 숫자로 변환시켜주었다
#    print("Hello 11 RAKA")                      # 숫자 11을 입력하면 input(11)="11" -> int("11")=11 이 된다. 문자는 숫자로 바꿀수없어 Error가 발생한다
else:
    print("Get Out!")
