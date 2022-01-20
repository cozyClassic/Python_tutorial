import os


"""

print(os.ctermid()) 
# 프로세스의 제어 터미널에 해당하는 파일명 반환
# /dev/tty

print(os.environ)
# dictonary 반환 : USER, COMMAND)_MODE, LOGNAME, PATH, SHELL, HOME, ... 등등

print(os.environb)
# os.environ의 byte버전


# os.fsencode()
print(os.getcwd())
# 현재 디렉토리 출력
# /Users/pro/Desktop/Codings/Python/official_docs

os.chdir('/Users/pro/Desktop/Codings/Python/')
# 입력한 path로 디렉토리 변경
print(os.getcwd())
# /Users/pro/Desktop/Codings/Python


print(os.listdir())
# 현재 위치에서 ls를 하되 디렉토리(폴더)만 출력

# os.mkdir('mkdir_test')
# os.makedirs('mkdir_test2')
# 디렉토리(폴더) 생성하기 (mkdir == makedirs)
# 이미 있는 파일일 경우 에러 발생

os.rmdir('mkdir_test')
os.removedirs('mkdir_test2')
# 디렉토리(폴더) 삭제 : 현재 경로에서


os.rename('test2.py', 'new_test.py')
# 파일명 변경
# os.rename(변경할 파일명, 새로운 파일명)


print(os.stat('new_test.py'))
# 파일의 상태를 반환한다.
# os.stat_result(st_mode=33188, st_ino=3036615, st_dev=16777221, st_nlink=1, st_uid=501, st_gid=20, st_size=301, st_atime=1642638051, st_mtime=1642399122, st_ctime=1642638051)

print(os.stat('new_test.py').st_mode)
# 이렇게 특정 데이터만 출력하는 것도 가능함

from datetime import datetime
print(datetime.fromtimestamp(os.stat('new_test.py').st_ctime))
# 이렇게 생성일을 출력하는 것도 가능하다.

for dirpath, dirnames, filenames in os.walk('/Users/pro/Desktop/Codings/Python/official_docs') :
    print('현재 경로 : ', dirpath)
    print('폴더 : ', dirnames)
    print('파일 : ', filenames)
    print()

# 특정 경로 내부의 디렉토리에 있는 하위 파일/폴더 목록 제공



HOME_DIRECTORY = os.environ.get('HOME')
print(HOME_DIRECTORY)
# environ : 환경변수
# /Users/pro


file_path = os.path.join(HOME_DIRECTORY, 'test.txt')
print(file_path)
# /Users/pro/test.txt
# file_path를 활용하는 방법 : 파일 열기
# with open(file_path, 'w') as f :

"""

# path 활용법
print(os.path.basename('/tmp/test.txt'))
# basename : 파일명 
# test.txt

print(os.path.dirname('/tmp/test.txt'))
# dirname : 경로명
# /tmp

print(os.path.split('/tmp/test.txt'))
# split : 각각 출력하기
# ('/tmp', 'test.txt')

print(os.path.exists('/tmp/test.txt'))
# exists : 파일이 존재하는지 확인하기
# False

print(os.path.exists(os.getcwd()))
# True

print(os.path.isdir(os.getcwd()))
# 이게 경로인가?
# True

print(os.path.isfile(os.getcwd()))
# 이게 파일인가?
# False

print(os.path.isfile(os.getcwd()+'/new_test.py'))
# True
# !주의 : 만약 존재하지 않는 파일이면 False를 반환한다.

print(os.path.splitext('/tmp/test.txt'))
# splitext : 확장자명 (extension?) 분리하기
# ('/tmp/test', '.txt')

