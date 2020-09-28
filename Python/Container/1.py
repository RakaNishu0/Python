print(type('RakaNishu'))
name = 'RakaNishu'
print(name)

print(type(['Raka', 'Nishu', 'Ho~']))

names = ['Raka', 'Nishu', 'Ho~']
# List의 원소(Element)는 []로 묶인다. 반드시 문자열만 오는 것은 아니다.

print(names)

# index는 0부터 시작한다.
print(names[1])

RakaNishu = ['Man', 'Old', 22, False]           # List의 데이터는 문자, 숫자 등 여러 종류가 가능하다
RakaNishu[2] = 36                               # index 2의 데이터를 36으로 치환한다

RakaNishu.append('No Manner')                   
print(len(RakaNishu))
print(RakaNishu)
