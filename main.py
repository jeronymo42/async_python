import time
import threading


def get_data(data):
    while True:
        print(f'{threading.currentThread().name} - {data}')
        time.sleep(5)


thr = threading.Thread(target=get_data, args=(str(time.time()),), name='first_thr')
thr.start()

for i in range(100):
    print(i)
    time.sleep(1)
