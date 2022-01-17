import os

print(os.access())

# print(os.chdir(path)) 
# 무슨 함수인지 모르겠음
# 현재 작업 디렉터리를 path로 변경한다.
# 이 함수는 파일 기술자 지정을 지원할 수 있다.

""" file descriptor 지정
 path 인자는 파일 경로를 지정하는 문자열이어야 한다.
 하지만, 일부 함수는 path 인자로 open file descriptor를 받아들인다.
 그러면 그 함수는 descriptor가 참조하는 파일에서 작동한다.
 (POSIX 시스템에서, 파이썬은 함수의 f 접두어가 붙은 함수의 변종을 호출한다.)
 (예를 들어, chdir 대신 fchdir)

 os.supports_fd를 사용하여, 사용자의 플랫폼에서 특정 함수에
 file descriptor로 path를 지정할 수 있는지를 확인할 수 있다.
 사용할 수 없을 때, 사용하면 NoImplementedError를 발생시킨다.

 함수가 dir_fd나 follow_symlinks인자도 지원하면, path에 파일 디스크립터를 제공할 대
 이 중 하나를 지정하는 것은 에러이다.
"""

# print(os.fchdir(fd)) 
# 무슨 함수인지 모르겠음

# print(os.getcwd())

# print(os.supports_fd)
# 함수로만 꽉 차있음
# chown, utime, stat, chdir, truncate, chmod, pathconf, statvfs

""" file descripotr에 대한 상대경로
 dir_fd가 None이 아니면, 디렉토리를 사리키는 file descriptor이여야 한다.
 경로는 상대경로여야 한다. 그러면 경로는 해당 디렉토리에 상대적이다.
 절대적이면, dir_fd는 무시된다.
 POSIX 시스템에서, 파이썬은 at 접미사를 붙이거나 어쩌면 f 접두사를 붙인 함수의 변종을 호출한다.
 예를 들어, access 대신 faccessat을 호출한다.

 os.supports_dir_fd를 사용하여, 사용자의 플랫폼에서 특정 함수에 dir_fd가 지원되는지를 확인할 수 있다.
 사용할 수 없을 때, 사용하면 NoImplementedError를 발생시킨다. 
"""

""" 심볼릭 링크를 따르지 않음
follow_symlinks가 False이고, 대상 경로의 마지막 요소가 심볼릭 링크이면
함수는 링크가 가리키는 파일 대신 심볼릭 링크 자체에 대해 작동한다.

"""

print(os.getcwd())