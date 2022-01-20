# 강의 주소 : https://www.youtube.com/watch?v=3QiPPX-KeSc

import socket
import threading

PORT = 5050

HOST_NAME = socket.gethostname()
print(HOST_NAME)
# proui-MacBookPro.local

SERVER = socket.gethostbyname(HOST_NAME)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
