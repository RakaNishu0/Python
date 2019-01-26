inp_value = input("Your ID..? : ")      # python의 input()은 문자열로만 반환한다.

real_raka = 11
real_nishu = "nishu"

if real_raka == inp_value:              # 문자열 vs 숫자의 비교이므로 False
    print("Hello raka")
elif real_nishu.upper() == inp_value.upper():
    print("Hello nishu")
else:
    print("Get Out!")
