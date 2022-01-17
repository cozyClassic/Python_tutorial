
# 7.2 Read, Write File의 내용
# nodeJS에서 fs(File System)으로 쓰던 기능을 갖고있는듯.

# 터미널처럼 ..로 상대경로 설정 가능.
f = open('../test') 

# head 또는 파일정보 읽어오기.
#print(f)
# 타입 = class : TextIoWrapper
#print(type(f))
# 파일 내의 데이터를 텍스트 형태로 읽기
# print(f.read()) 

# 파일내의 텍스트를, "line"을 기준으로 읽어온다. 여기에는 개행문자가 포함된다.
#print(f.readline())
#print(f.readline())
#print(f.readline())
#print(f.readline())

#현재 읽고있는 현재 위치 알기 :: 세로 줄 기준이 아닌 문자 하나하나를 세서 숫자를 구함.

#print(f.tell())

#f.seek(5)
#print(f.readline())

# 파일을 열고나면 꼭 닫을 것.
#f.close()
# 버퍼 사이즈를 불러오기.
import json
"""
x = [1, 'simple', 'list']
print(json.dumps(x))
# 결과 : [1, "simple", "list"]

# json으로 바꾸면 데이터 타입이 str로 변경된다.
print(type(json.dumps(x))) 

f = open('../test')
# 파일 불러오기.
x = json.load(f)

#123456789
print(x)

#데이터 타입이 자동으로 int로 바뀌어 있음.
print(type(x))

print(json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':')))
"""
