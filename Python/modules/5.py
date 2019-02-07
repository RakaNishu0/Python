import auth             ## auth 파일을 모듈로써 불러온다.

input_id = input("Your ID..? : ")

if auth.login(input_id):            ## auth 모듈 안의 login() 함수를 사용
    print('Hello '+input_id)
else:
    print('Who Are You?')
