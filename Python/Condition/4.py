inp_value = 11

real_raka = 11
real_nishu = 22

if real_raka == inp_value:
    print("Hello raka")
elif real_nishu == inp_value:       # elif = elseif / if의 조건이 False일 때에 다시 한번 실행될 조건을 지정 / elif는 복수설정 가능
    print("Hello nishu")            # elif 의 조건이 True일 때 실행되는 부분
else:
    print("Get Out!")               # else 는 elif의 조건마저도 False일 때 출력할 결과를 지정하게 된다
