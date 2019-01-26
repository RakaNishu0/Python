input_id = input("Your ID..? : ")      # python의 input()은 문자열로만 반환한다.
input_id2 = input("Your PW..? : ")

real_id = "raka"
real_id2 = "nishu"

if real_id == input_id or real_id2 == input_id2:
    print("Hello raka or nishu")
else:
    print("Get Out!")
