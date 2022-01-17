import time

a = "RANDOM"

for i in a :
    print(i, end = " ")
    time.sleep(0.3)

# 이 상태로는 하나씩 출력되는 것이 아닌, 한번에 출력이 됨.

for i in a :
    print(i, end = " ", flush=True)
    time.sleep(0.3)

    