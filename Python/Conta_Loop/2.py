members = ['Raka', 'Nishu', 'Ho~', 'Yo~~']

# i = 0                         # while 은 for ~ in 과 다른 점은 대부분의 언어에서 반복문의 기본으로 정착되어 있다는 점
# while i < len(members):       # for ~ in 은 언어에 따라 지원하지 않는 경우도 있다
#     print(members[i])         # 반복문의 기본적인 성질 / 활용에 대한 개념은 while 을 통해 익히는 것이 기본
#     i= i + 1

for a in members:       # for ~ in 구문은 while과 달리, 실행조건이라기보다 리스트의 데이터를 {a}에 대입시키는 것을 반복한다는 의미가 된다
    print(a)            # while과 달리 단 2줄이면 위와 같은 결과를 나타낼 수 있다.
