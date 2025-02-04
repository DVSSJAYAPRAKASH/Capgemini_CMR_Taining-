import threading
import time

def task(lock):
    with lock:
        print(f"{threading.current_thread().name} acquired the lock")
        time.sleep(2)
        print(f"{threading.current_thread().name} released the lock")
lock=threading.Lock()
thread1=threading.Thread(target=task,args=(lock,))
thread2=threading.Thread(target=task,args=(lock,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()

