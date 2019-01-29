# python의 input()은 문자열로만 반환한다.

#members = ['raka','nishu','luke','skywalker']
# for id in members:
#     if id == inp_value:
#         print("Hello "+inp_value)
#         import sys
#         sys.exit()
# print("Who Are You?")

# real_raka = 11
# real_nishu = "nishu"
#
# if real_raka == inp_value:              # 문자열 vs 숫자의 비교이므로 False
#     print("Hello raka")
# elif real_nishu.upper() == inp_value.upper():
#     print("Hello nishu")
# else:
#     print("Get Out!")

##### Function #####
# str = input('str 1 = ')
# num = input('str 2 = ')
#
# def make_string(str, num):
#     return str+num
#
# print(make_string(str, num))
#####################

input_id = input("Your ID..? : ")

def login(i):
    members = ['raka','nishu','luke','skywalker']
    for user in members:
        if user == i:
            return True         # return은 결과값을 받는다. + return 이후의 문단은 무의미하다.
    return False                # return 으로 반환된 결과를 여러 곳에 여러 용도로 활용할 수 있다.


if login(input_id):
    print('Hello '+input_id)
else:
    print('Get Out..!!!')
