# python의 input()은 문자열로만 반환한다.

# members = ['raka','nishu','luke','skywalker']
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


def login(i):                                               # 함수 login() 을 정의하려 한다. i 라는 변수에 입력값을 받을 예정
    members = ['raka', 'nishu', 'luke', 'skywalker']        # 리스트를 만들고
    for user in members:                                    # 리스트의 데이터를 user 라는 변수에 넣는다
        if user == i:                                       # user 라는 변수와 i 라는 입력값(변수)이 같은가?를 비교한다
            return True                                     # 참이라면 True 를 반환하고
    return False                                            # 거짓이라면 False 를 반환하는 것으로 함수를 종료한다


if login(input_id):                                         # 실제 함수를 실행하는 부분. login()의 입력값은 위의 input_id 로 받아서 입력(=str)
    print('Hello '+input_id)                                # 참이라면 프린트
else:
    print('Get Out..!!!')                                   # 거짓이라면 프린트하고 프로그램을 종료
