# print('Hello World 0')
# print('Hello World 9')
# print('Hello World 18')
# print('Hello World 27')
# print('Hello World 36')
# print('Hello World 45')
# print('Hello World 54')
# print('Hello World 63')
# print('Hello World 72')
# print('Hello World 81')

i = 0
while i < 10:           # while 의 뒤에는 Boolean 이 따라와야 한다 (True or False)
    print("print('Hello World "+str(i*9)+"')")      # i*9 는 숫자데이터인데, 문자열 사이에 합칠 수 없으므로 이를 문자열(str)화 하여야 한다
    i = i+1
print("while Ended")
