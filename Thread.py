import time , threading

ticket = 10

def loop():
    global ticket
    print(f'thread {threading.current_thread().name} is running...')
    n = 0
    while ticket > 0:
        ticket = ticket - 1
        print(f'thread {threading.current_thread().name} >>> {ticket}')
        time.sleep(1)
    print(f'thread {threading.current_thread().name} ended')

print(f'thread {threading.current_thread().name} is running...')
t = threading.Thread(target = loop)
t2 = threading.Thread(target = loop)
t3 = threading.Thread(target = loop)
t.start()
t2.start()
t3.start()
t.join()
t2.join()
t3.join()
print(f'thread {threading.current_thread().name} ended')
