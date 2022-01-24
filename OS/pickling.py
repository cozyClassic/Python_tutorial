from copyreg import pickle
import pickle

# pickle 모듈 : dump(), load() 함수 제공
# 객체 <-> 파일간의 데이터 전송 기능
# dump() 함수 : 네트워크에 전송할 수 있도록 변환하는 작업 (seriliaztion 또는 pickling) 제공
# load() 함수 : 바이트 스트림을 객체로 변환하는 작업 (역직렬화, unpickling)
# 바이트 IO를 위해 rb 모드, 또는 wb 모드를 사용한다.


Pres = { "Kennedy" : 35, "Obama" : 44}

# 딕셔너리를 피클 파일에 저장
pickle.dump(Pres, open("pres.pic", "wb"))

# 피클 파일에 딕셔너리를 로딩

Pres2 = pickle.load(open("pres.pic", "rb"))
Pres2['Trump'] = 45

pickle.dump(Pres2, open("pres2.pic", "wb"))
print(Pres)
print(Pres2)