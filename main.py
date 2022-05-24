import requests
from time import time, ctime, sleep

def tx():
        t=time()
        time_list=ctime(t).split()
        hours_list = time_list[3].split(':')
        return hours_list

print(tx())

while True:
        hours_list=tx()
        if int(hours_list[0])<=21 and int(hours_list[0])>=7:
                print('start requestowania .....')
                r = requests.get('https://dawidciupka.herokuapp.com')
                print(r)
                z = requests.get('https://what-tomorrow.herokuapp.com')
                print(z)

                print(f'ok time: {tx()}')
                sleep(1735)
                print('koniec odliczania 1735')
        else:
                continue

