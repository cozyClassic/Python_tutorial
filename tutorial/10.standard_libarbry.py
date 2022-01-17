#import os
# 주의점 : os.
#import statistics
#data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

#print(statistics.mode(data))

# import urllib.request
# with urllib.request.urlopen('https://python.org/') as response:
#    html = response.read()

# 접속을 하는것 같기는 한데 SSL 보안에 자꾸 걸린다.

# 현재 urllib.request 는 https 형태로 접속하는 것이 불가능하다고 한다.
# import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('nzlk112@gmail.com', 'km0192@naver.com',
# """To: jcaesar@example.org
# From: soothsayer@example.org
# ...
# Beware the Ides of March.
# """)
# server.quit()

# 이것도 역시 아무런 기본세팅을 하지 않은채로는 gmail에 접속하는게 안된다고 나타난다.
# ConnectionRefusedError: [Errno 61] Connection refused



#from timeit import Timer
#Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()

# import doctest
# def average(values) :
#     """
#     This function return the 'average' of values.

#     Example
#     -------
#     >>> average([50,100,150])
#     100
#     """

#     return(sum(values)/len(values))


# doctest.testmod()

# from string import Template
# t = Template('${village}folk send $$10 to $cause.')
# print(t.substitute(village='Nottingham', cause='the ditch fund'))


# import struct

# texts = "ABCDEFG"
# fields = struct.pack(texts)
# print(fields)

# import logging
# logging.debug('Debugging information')
# logging.info('Informational message')
# logging.warning('Warning:config file %s not found', 'server.conf')
# logging.error('Error occurred')
# logging.critical('Critical error -- shutting down')


from array import array

a = array('H', [1,2,3,4,5])
print(sum(a))
# 15
print(a[1:3])
# array('H', [2, 3])

# b = array('H', [1,"A"])
# 에러 반환.