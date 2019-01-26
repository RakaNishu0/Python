input_id = input("Your ID..? : ")      # python의 input()은 문자열로만 반환한다.
#input_pw = input("Your PW..? : ")

real_id = "raka"
real_pw = "1111"

if real_id == input_id and real_pw == input("Your PW..? "):
    print("Hello raka with 1111")
else:
    print("Get Out!")
